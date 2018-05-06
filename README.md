# DesafioPython
## Task


Caminho padrão : http://127.0.0.1:8000/

- Foi desenvolvida uma aplicação back end :
- Lista de filmes (Com paginação):
- Lista filmes http://127.0.0.1:8000/filmes/
 
 {
    "count":numbet ,
    "next": string,
    "previous": string,
    "results": [
        {
            "url":hateoas_url,
            "id": number,
            "title": string,
            "original_title": string,
            "slug": string,
            "synopsis": string,
            "duration_in_seconds": number,
            "image": string,
            "likes": number,
            "published": bolean,
            "owner": string,
            "actors": object
        }]
  }

 
 - Lista atores http://127.0.0.1:8000/actors/ 

 {
    "count": number,
    "next": string,
    "previous": string ,
    "results": [
        {
            "id": number,
            "name": string,
            "age": number,
            "filme": string
        }
    ]
}
 - Mostra os detalhes http://127.0.0.1:8000/actors/1/
 - Api root http://127.0.0.1:8000/ :
  {
      "users": "http://127.0.0.1:8000/users/",
      "filmes": "http://127.0.0.1:8000/filmes/",
      "actors": "http://127.0.0.1:8000/actors/"
  }
  - Buscar por slug http://127.0.0.1:8000/filmes/{slug}/
  - Buscar por id http://127.0.0.1:8000/filmes/{id}/
  - Busca por ordenação http://127.0.0.1:8000/filmes/findAllOrderBy?type={tipoCampo}
  - Incrementar curtidas por id http://127.0.0.1:8000/filmes/likeMovie/{id}
  - Incrementar curtidas por id http://127.0.0.1:8000/filmes/likeMovie/{slug}
 
  Foi implementado também em Filmes POST, PUT, DELETE, PATCH
  POST http://127.0.0.1:8000/filmes/   

     {
        "title": string,
        "original_title": string,
        "slug": string,
        "synopsis": string,
        "duration_in_seconds": number,
        "image": string,
        "likes": number,
        "published": bolean,
        "owner": string
     }


     PUT http://127.0.0.1:8000/filmes/{id}  ou http://127.0.0.1:8000/filmes/{slug}

     {
        "title": string,
        "original_title": string,
        "slug": string,
        "synopsis": string,
        "duration_in_seconds": number,
        "image": string,
        "likes": number,
        "published": bolean,
        "owner": string
     }


    DELETE http://127.0.0.1:8000/filmes/{id}  

    PATCH http://127.0.0.1:8000/filmes/likeMovie/{id}
    PATCH http://127.0.0.1:8000/filmes/likeMovie/{slug}
  

  Foi implementado também em Actor POST, PUT, DELETE, PATCH

   http://127.0.0.1:8000/actors/   

        {
            "id": number,
            "name": string,
            "age": number,
            "filme": {Object}
        }


    PUT http://127.0.0.1:8000/actors/{id}   

        {
            "name": string,
            "age": number,
            "filme": {Object}
        }
    
    DELETE http://127.0.0.1:8000/actors/{id}   


## Instalação
Sistema operacional Mac Os / Ubuntu 

 https://docs.docker.com/docker-for-mac/install/
 É necessário instalar o  docker  no sistema 

## Testes
Execute o comando para rodar os tests:
python manage.py test filmes.tests

## Iniciar Projeto
Na pasta raiz do projeto execute os comandos:
- docker-compose build
- docker-compose up -d
Execute : python manage.py runserver

Área administrativa /admin {Existe uma funcionalidade na api padrao django rest framework  http://127.0.0.1:8000/api-auth/login/?next=/filmes/admin/   usuário default :{ user :disalles7 password : Disilva@220 }

Acesso completo a api
