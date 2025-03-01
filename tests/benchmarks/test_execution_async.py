import asyncio
from graphql import (
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLField,
    GraphQLString,
    graphql,
)


user = GraphQLObjectType(
    name="User",
    fields={
        "id": GraphQLField(GraphQLString),
        "name": GraphQLField(GraphQLString),
    },
)


async def resolve_user(obj, info):
    return {
        "id": "1",
        "name": "Sarah",
    }


schema = GraphQLSchema(
    query=GraphQLObjectType(
        name="Query",
        fields={
            "user": GraphQLField(
                user,
                resolve=resolve_user,
            )
        },
    )
)


def test_execute_basic_async(benchmark):
    result = benchmark(
        lambda: asyncio.run(graphql(schema, "query { user { id, name }}"))
    )
    assert not result.errors
    assert result.data == {
        "user": {
            "id": "1",
            "name": "Sarah",
        },
    }
