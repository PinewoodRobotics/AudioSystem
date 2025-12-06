import subprocess

subprocess.Popen([
    'shairport-sync',
    '-a', 'PEARL',
    '--',
    '-d', 'plughw:CARD=MobilePre,DEV=0'
])

input()

process.terminate()

