param ($file)

Start-Process "python" -ArgumentList "transpile.py $file" -Wait -NoNewWindow
Start-Process "python" -ArgumentList "outputfilefilefile.py" -Wait -NoNewWindow

Remove-Item "outputfilefilefile.py"