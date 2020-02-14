from gql import gql

gql_create_model = gql("""
mutation CreateModel($name: String!) {
  createModel(name: $name) {
    id
  }
}
""")


gql_create_datapoint = gql("""
mutation CreateDataPoint($epoch: Int!, $loss: Float!, $acc: Float!) {
  createDataPoint(epoch: $epoch, loss: $loss, acc: $acc) {
    id
  }
}
""")

gql_connect_datapoint_with_model = gql("""
mutation AddToDataPointOnModel($modelModelId: ID!, $dataPointsDataPointId: ID!) {
  addToDataPointOnModel(
    modelModelId: $modelModelId,
    dataPointsDataPointId: $dataPointsDataPointId
  ) {
    modelModel{
      id
    }
    dataPointsDataPoint{
      id
    }
  }
}
""")
