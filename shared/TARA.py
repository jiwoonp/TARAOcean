def OGAsubmit(requestName, sequence):
    import subprocess
    cmd = './shared/OGAsubmit.sh'
    run_cmd = [cmd, requestName, sequence]
    proc = subprocess.run(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(50*'=')
    print('*** screen output from worker:\n')
    print(proc.stdout.decode())
    print(50*'=')
    print('*** error messages from worker:\n')
    print(proc.stderr.decode())
    print(50*'=')