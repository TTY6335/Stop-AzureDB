# StopAzureDB
Azure Functions for stopping Azure Database Services on scheduled time.  
Azure Databse for MySQL, Azure Databse for MySQL - flexible server, Azure Databse for PostgreSQL, Azure Databse for PostgreSQL - flexible serverをスケジュールを利用して停止するAzure Functionsの関数アプリになります。  
詳しい説明は[こちら](https://tty6335.hatenablog.com/entry/2023/11/05/121318?_gl=1*c1jm51*_gcl_au*MTQ1NTE1MTk1NS4xNjk2MjUwNDQy)  

This is an Azure Functions function app for stopping Azure Database Services on a scheduled time. It is designed to use scheduling to stop Azure Database for MySQL, Azure Database for MySQL - flexible server, Azure Database for PostgreSQL, and Azure Database for PostgreSQL - flexible server. For more detailed information, please click [here](https://tty6335.hatenablog.com/entry/2023/11/05/121318?_gl=1*c1jm51*_gcl_au*MTQ1NTE1MTk1NS4xNjk2MjUwNDQy).

# How to Use
Clud Shellまたはazure-cliを利用して作成することを想定しています。  
This is intended to be created using Azure Cloud Shell or the azure-cli.  
## 関数アプリ作成 Make Function App  
関数アプリの情報を書き込むストレージアカウントを作成します。  
Create a storage account to store information for the function app.  
``` sh
$ az storage account create --name <STORAGE_NAME> --location <REGION> --resource-group <RESOURCE_GROUP> --sku Standard_LRS
```
関数アプリを作成します。ここではStopDBとします。  
Create the function app. Let's name it "StopDB."
``` sh
$ az functionapp create --resource-group  <RESOURCE_GROUP> ---consumption-plan-location <REGION> --runtime python --runtime-version 3.9 --functions-version 4 --name StopDB --os-type linux --storage-account <STORAGE_NAME>
```

## スクリプト編集 Edit Script  
GitHubからスクリプトをcloneし、function_app.pyを編集します。 MySQLの場合はStopMySQL、PostgreSQLの場合はStopPostgreSQLの配下のものを使用してください。  
function_app.pyではサブスクリプションID(13行目)、リソースグループ名(16行目)を入力し、起動時刻をUTCでセット(21行目)します。

Clone the script from GitHub and edit the `function_app.py`. We'll use the appropriate script under "StopMySQL" for MySQL and "StopPostgreSQL" for PostgreSQL. In the `function_app.py`, you need to input the Subscription ID (line 13), the Resource Group name (line 16), and set the startup time in UTC (line 21).

## スクリプトデプロイ Deploy Script  
以下のコマンドでデプロイします。 Remote build succeeded!と表示されるまで待機します。  
You can deploy using the following command and wait until you see "Remote build succeeded!":  
``` sh
$ func azure functionapp publish StopDB
```

## カスタムロール作成/付与  Create and Assign the Custom Role   
関数アプリに付与するカスタムロールを作成します。この関数アプリがDBを操作するために必要な権限は、読み取り権限と停止する権限のみです。  
RBACディレクトリの中にあるjsonファイルを参考にして作成してください。  
Create a custom role to be assigned to the function app. The only permissions required for this function app to operate on databases are read and stop permissions. Please refer to the JSON files within the RBAC directory when creating this custom role.
