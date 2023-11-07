# Fighter Jet!

## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要
- シューティングゲーム
- 敵は白・緑・赤
- スコアは時間経過と敵を倒したら加算
  - 白(+1)・緑(+10)・赤(+20)
- 白と緑の雑魚キャラを一定時間が経過するごとに召喚

## 操作方法
- [space]キー: 自機がビームを発射
- [e]キー: 敵機のビームを発射
- [g]キー: greenレベルの敵を召喚
- [r]キー: redレベルの敵を召喚

## ゲームの実装
### 共通基本機能
- 背景スクロール機能

### 担当追加機能
- C0B22149
  - キャラの実装
  - 敵機と自機の当たり判定
- C0B22077
  - タイトル画面
  - ゲーム開始とゲーム終了ボタンを配置
- C0A22127
  - 敵機の実装
  - 敵機とビームの当たり判定
- C0A22151
  - タイマーとスコア関数
- C0A22023
  - GAMEOVER画面の実装

## メモ
1. ビームを上に打つ
2. [r]を押して，高得点を出せるキャラを召喚
3. 隙をみて，敵機を殺す
