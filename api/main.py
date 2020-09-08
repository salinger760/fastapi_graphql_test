import graphene

from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from models import db_session
from schema import schema


# Grapheneを利用したGraphQLスキーマを作成する
class Query(graphene.ObjectType):
    # 引数nameを持つフィールドhelloを作成
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    # フィールドhelloに対するユーザへ返すクエリレスポンスを定義
    def resolve_hello(self, info, name):
        return "Hello " + name


# FastAPIを利用するためのインスタンスを作成
app = FastAPI()
# GraphQLのエンドポイント
# app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))

app.add_route("/graphql", GraphQLApp(schema=schema))

# APIサーバシャットダウン時にDBセッションを削除
@app.on_event("shutdown")
def shutdown_event():
    db_session.remove()