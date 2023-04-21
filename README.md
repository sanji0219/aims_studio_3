# aims_studio_3

## リポジトリの作成
1. GitHubにログインし、ダッシュボードに移動します。
2. New repositoryをクリックします。
3. Repository nameにリポジトリの名前を入力し、Descriptionにリポジトリの説明を追加します。
4. リポジトリの種類を選択します。公開リポジトリは誰でもアクセスできますが、プライベートリポジトリは招待されたユーザーしかアクセスできません。
5. Create repositoryをクリックして、リポジトリを作成します。

## リポジトリのフォーク
1. リポジトリにアクセスします。
2. Forkをクリックして、自分のアカウントにリポジトリをフォークします。
3. フォークされたリポジトリは、GitHubの自分のアカウント内に作成されます。

## プルリクエストの送信
1. リポジトリにアクセスし、Forkをクリックして、自分のアカウントにリポジトリをフォークします。
2. ローカルマシンにリポジトリをクローンします。git clone https://github.com/your-username/repository-name.git
3. 新しいブランチを作成します。git checkout -b new-branch-name
* 多分、ここでgit add .が必要
4. 変更を加え、変更内容をコミットします。git commit -m "commit message"
5. リモートリポジトリに新しいブランチをプッシュします。git push origin new-branch-name
6. GitHubに戻り、Compare & pull requestをクリックします。
7. 変更内容を確認し、説明を追加します。
8. Create pull requestをクリックして、プルリクエストを送信します。