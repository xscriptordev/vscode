const { workspace, window, commands } = require('vscode');

function activate(context) {
  const config = () => workspace.getConfiguration('xglass');

  // Will be defined according to the platform, but accessible for commands
  let setAlpha = () => window.showErrorMessage('xglass: unsupported platform.');

  if (process.platform === 'win32') {
    let ps = null;
    let typeLoaded = false;

    const ensureWinReady = async () => {
      if (!ps) {
        const shell = require('node-powershell');
        ps = new shell({ executionPolicy: 'RemoteSigned', noProfile: true });
        context.subscriptions.push(ps);
      }
      if (!typeLoaded) {
        const path = context.asAbsolutePath('./SetTransparency.cs');
        ps.addCommand('[Console]::OutputEncoding = [Text.Encoding]::UTF8');
        ps.addCommand(`Add-Type -Path '${path}'`);
        await ps.invoke().finally(() => { ps.commands = []; });
        typeLoaded = true;
      }
    };

    setAlpha = async (alpha) => {
      try {
        if (alpha < 1) alpha = 1;
        else if (alpha > 255) alpha = 255;

        await ensureWinReady();

        // Correct C# method name! SetTransparency
        ps.addCommand(`[xglass.SetTransParency]::SetTransparency(${process.pid}, ${alpha})`);
        await ps.invoke().finally(() => { ps.commands = []; });

        console.log(`xglass: set alpha ${alpha}`);
        await config().update('alpha', alpha, true);
      } catch (err) {
        console.error(err);
        window.showErrorMessage(`xglass Error (win32): ${err}`);
      }
    };
  } else if (process.platform === 'linux') {
    const cp = require('child_process');

    let codeWindowIds = [];
    try {
      cp.spawnSync('which', ['xprop'], { stdio: 'ignore' });

      const processIds = cp.execSync(`pgrep 'code'`).toString().trim().split('\n').filter(Boolean);
      const allWindowIdsOutput = cp.execSync(`xprop -root | grep '_NET_CLIENT_LIST(WINDOW)'`).toString();
      const allWindowIds = (allWindowIdsOutput.match(/0x[\da-f]+/ig) || []);

      for (const windowId of allWindowIds) {
        const hasProcessId = cp.execSync(`xprop -id ${windowId} _NET_WM_PID`).toString();
        if (!(hasProcessId.search('not found') + 1)) {
          const winProcessId = hasProcessId.replace(/([a-zA-Z_()\\s=])/g, '');
          if (processIds.includes(winProcessId)) codeWindowIds.push(windowId);
        }
      }

      setAlpha = (alpha) => {
        if (alpha < 1) alpha = 1;
        else if (alpha > 255) alpha = 255;

        for (const id of codeWindowIds) {
          cp.exec(
            `xprop -id ${id} -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY $(printf 0x%x $((0xffffffff * ${alpha} / 255)))`,
            async (error) => {
              if (error) {
                console.error(error);
                window.showErrorMessage(`xglass Error (linux): ${error.message}`);
                return;
              }
              console.log(`xglass: set alpha ${alpha}`);
              await config().update('alpha', alpha, true);
            }
          );
        }
      };
    } catch (e) {
      console.error(e);
      setAlpha = () => window.showErrorMessage('xglass Error: xprop / windows not available.');
    }
  }

  console.log('xglass VSC active');

  // ---- Commands (trigger activation) ----
  context.subscriptions.push(commands.registerCommand('xglass.enable', () => {
    setAlpha(200); // activate and set alpha=200
  }));

  context.subscriptions.push(commands.registerCommand('xglass.increase', () => {
    const alpha = config().get('alpha') - config().get('step');
    setAlpha(alpha);
  }));

  context.subscriptions.push(commands.registerCommand('xglass.decrease', () => {
    const alpha = config().get('alpha') + config().get('step');
    setAlpha(alpha);
  }));

  context.subscriptions.push(commands.registerCommand('xglass.max', () => setAlpha(1)));
  context.subscriptions.push(commands.registerCommand('xglass.min', () => setAlpha(255)));

}

exports.activate = activate;
function deactivate() {}
exports.deactivate = deactivate;
