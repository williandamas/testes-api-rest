from httpx import delete, get, post

url_base = 'http://localhost:5000/todos/api/tasks'

request = get(url_base)

# assert request.status_code == 200, 'Código de resposta diferente de 200'
# assert request.json() == [], 'Algo de errado não está certo com esse recurso'

not_task = {'titulo': 'Aprender'}
bad_task = {'tittle': 'Aprender'}
good_task = {'tittle': 'Aprender', 'description': 'Porque preciso', 'done': False}


# request = post(url_base, json=not_task)
# assert request.status_code == 400, 'Código de resposta diferente de 400'
#
# request = post(url_base, json=bad_task)
# assert request.status_code == 400, 'Código de resposta diferente de 400'
#
# request = post(url_base, json=good_task)
# assert request.status_code == 201, 'Código de resposta diferente de 201'

request = delete(url_base + '/2')
assert request.status_code == 204, 'O código esta diferente de 204'
