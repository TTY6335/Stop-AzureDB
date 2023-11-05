# StopAzureDB
Azure Functions for stopping Azure Database Services on scheduled time.  
Azure Databse for MySQL, Azure Databse for MySQL - flexible server, Azure Databse for PostgreSQL, Azure Databse for PostgreSQL - flexible serverをスケジュールを利用して停止するAzure Functionsの関数アプリになります。  
詳しい説明は[こちら](https://tty6335.hatenablog.com/entry/2023/11/05/121318?_gl=1*c1jm51*_gcl_au*MTQ1NTE1MTk1NS4xNjk2MjUwNDQy)

# How to Use
Clud Shellまたはazure-cliを利用して作成することを想定しています。  
## 関数アプリ作成  
関数アプリの情報を書き込むストレージアカウントを作成します。  
``` sh
$ az storage account create --name <STORAGE_NAME> --location <REGION> --resource-group <RESOURCE_GROUP> --sku Standard_LRS
```
関数アプリを作成します。ここではStopDBとします。
``` sh
$ az functionapp create --resource-group  <RESOURCE_GROUP> ---consumption-plan-location <REGION> --runtime python --runtime-version 3.9 --functions-version 4 --name StopDB --os-type linux --storage-account <STORAGE_NAME>
```

## スクリプト編集  
GitHubからスクリプトをcloneし、function_app.pyを編集します。 MySQLの場合はStopMySQL、PostgreSQLの場合はStopPostgreSQLの配下のものを使用してください。  
function_app.pyではサブスクリプションID(13行目)、リソースグループ名(16行目)を入力し、起動時刻をUTCでセット(21行目)します。

## スクリプトデプロイ  
以下のコマンドでデプロイします。 Remote build succeeded!と表示されるまで待機します。  
``` sh
$ func azure functionapp publish StopDB
```

## カスタムロール作成/付与  
関数アプリに付与するカスタムロールを作成します。この関数アプリがDBを操作するために必要な権限は、読み取り権限と停止する権限のみです。  
RBACディレクトリの中にあるjsonファイルを参考にして作成してください。
