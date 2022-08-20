## Teste - Desenvolvimento de Software- JetBov 

### Endpoints para cadastro de gado com brincos e áreas para pastagens<br><br><br>

# Endpoints

# Áreas
## Cadastro
`POST  /area - FORMATO DA ENTRADA`

```JSON
{
	"area":"B",
	"gmd":1,
	"total_de_animais":2
}
```
Caso de tudo certo a resposta será

`POST /area - FORMATO DA SAÍDA - STATUS 201`

```JSON
{
	"animais_na_area": 0,
	"area": "B",
	"gmd": 0.8,
	"total_de_animais": 2
}
```

Possível erro:

Caso área já estiver cadastrada

`POST /area - FORMATO DA SAÍDA - STATUS 409`
```JSON
{
	"message": "Área já cadastrada"
}
```

# Listagem
`GET /areas - FORMATO DA SAÍDA - STATUS 200`
```JSON
[
    {
		"animais_na_area": 1,
		"area": "A",
		"gmd": 1,
		"total_de_animais": 2
	},
	{
		"animais_na_area": 0,
		"area": "B",
		"gmd": 0.8,
		"total_de_animais": 2
	}
]
```


# Gado
## Cadastro
`POST  /cattle - FORMATO DA ENTRADA`
```JSON
{
	"brinco":"a3",
	"peso_inicial":100,
	"area_inicial":"B",
	"dias_na_area":1
}
```
Caso de tudo certo a resposta será

`POST /cattle - FORMATO DA SAÍDA - STATUS 201`
```JSON
{
	"area_inicial": "B",
	"brinco": "a3",
	"data_de_entrada": "20/08/22",
	"data_de_saida": "28/08/22",
	"dias_na_area": 1,
	"peso_inicial": 150
}
```
Possiveis erros:

Caso brinco já estiver cadastrado

`POST /cattle - FORMATO DA SAÍDA - STATUS 409`
```JSON
{
	"message": "Brinco já cadastrado"
}
```
Caso área já estiver lotada

`POST /cattle - FORMATO DA SAÍDA - STATUS 401`
```JSON
{
	"message": "Já possui 2 animais na área selecionada"
}
```
Caso não existir área sitada

`POST /cattle - FORMATO DA SAÍDA - STATUS 409`
```JSON
{
	"message": "Área ainda não cadastrada"
}
```
# Listagem<br>

Caso existam animais cadastrados

`GET /cattles - FORMATO DA SAÍDA - STATUS 200`
```JSON
[
	{
		"area_inicial": "B",
		"brinco": "a3",
		"data_de_entrada": "19/08/22",
		"data_de_saida": "27/08/22",
		"dias_na_area": 1,
		"peso_inicial": 150
	},
    ...
]
```
Caso não existam animais cadastrados

`GET /cattles - FORMATO DA SAÍDA - STATUS 200`
```JSON
[]
```

# Listagem por brinco<br>

Caso existir brinco

`GET /cattle/<brinco> - FORMATO DA SAÍDA - STATUS 200`

`GET /cattle/a3`
```JSON
[
	{
		"area_inicial": "B",
		"brinco": "a3",
		"data_de_entrada": "19/08/22",
		"data_de_saida": "20/08/22",
		"dias_na_area": 1,
		"peso_final": 150.8,
		"peso_inicial": 150
	}
]
```
Possível erro:

Caso não exista o brinco cadastrado

`GET /cattle/<brinco> - FORMATO DA SAÍDA - STATUS 404`
```JSON
{
	"message": "Brinco não encontrado"
}
```

# Atualização por brinco<br>

Caso existir brinco

`PATCH /cattle/<brinco> - FORMATO DA ENTRADA`

`PATCH /cattle/a3`

```JSON
{
	"area":"A",
	"dias_na_area":5
}
```

Caso de tudo certo a resposta será

`PATCH /cattle/<brinco> - FORMATO DA SAÍDA STATUS 200`

`PATCH /cattle/a3`

```JSON
[
	{
		"area_inicial": "A",
		"brinco": "a3",
		"data_de_entrada": "19/08/22",
		"data_de_saida": "24/08/22",
		"dias_na_area": 5,
		"peso_final": 150.8,
		"peso_inicial": 155.8
	}
]
```

Possíveis erros:

Caso brinco não esteja cadastrado

`PATCH /cattle/<brinco> - FORMATO DA SAÍDA STATUS 404`

`PATCH /cattle/a35`

```JSON
{
	"message": "Brinco não encontrado"
}
```

Caso área não esteja cadastrada

`PATCH /cattle/<brinco> - FORMATO DA ENTRADA`

`PATCH /cattle/a3`

```JSON
{
	"area":"J",
	"dias_na_area":5
}
```

`PATCH /cattle/<brinco> - FORMATO DA SAÍDA STATUS 404`

`PATCH /cattle/a35`

```JSON
{
	"message": "Área não cadastrada"
}
```

Caso área já estiver lotada

`PATCH /cattle/<brinco> - FORMATO DA SAÍDA - STATUS 401`

`PATCH /cattle/a3`
```JSON
{
	"message": "Já possui 2 animais na área selecionada"
}
```
Caso animal já estiver na área selecionada

`PATCH /cattle/<brinco> - FORMATO DA ENTRADA`

`PATCH /cattle/a3`

```JSON
{
	"area":"A",
	"dias_na_area":5
}
```

`PATCH /cattle/<brinco> - FORMATO DA SAÍDA - STATUS 401`

`PATCH /cattle/a3`
```JSON
{
	"message": "Este animal já está nesta área"
}
```

# Deleção

Caso existir brinco

`DELETE /cattle/<brinco> - FORMATO DA REQUISIÇÂO`

`DELETE /cattle/a3`

Caso de tudo certo a respopsta será

`DELETE /cattle/<brinco> - FORMATO DA RESPOSTA STATUS 204`

`DELETE /cattle/a3`

Possível erro:

Caso não exista brinco

`DELETE /cattle/<brinco> - FORMATO DA REQUISIÇÂO`

`DELETE /cattle/a35`

A resposta será

`DELETE /cattle/<brinco> - FORMATO DA RESPOSTA 404`

`DELETE /cattle/a35`

```JSON
{
	"message": "Brinco não encontrado"
}
```