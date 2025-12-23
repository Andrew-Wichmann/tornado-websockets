import requests


resp = requests.post("http://localhost:5150/jobs")
resp.raise_for_status()
job_id = int(resp.content)

reps_content = ''
while reps_content != b'done!':
    resp = requests.get(f"http://localhost:5150/jobs/{job_id}/")
    print('timeout. trying again')
    reps_content = resp.content
