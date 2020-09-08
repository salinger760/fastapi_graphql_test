import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Department as DepartmentModel, Employee as EmployeeModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class DepartmentConnections(relay.Connection):
    class Meta:
        node = Department


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class EmployeeConnections(relay.Connection):
    class Meta:
        node = Employee


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # デフォルトでは、ソートが有効化されている
    all_employees = SQLAlchemyConnectionField(EmployeeConnections)
    # ソートを無効化
    all_departments = SQLAlchemyConnectionField(DepartmentConnections, sort=None)


schema = graphene.Schema(query=Query)
