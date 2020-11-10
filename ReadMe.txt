任意のIBCのData ConsumptionをExcelに出力するプログラムです。

<Input>
    Mainプログラムのurl変数の中に抽出したいIBCのURLを貼り付けてください。

<Output>
    プログラムと同じディレクトリにExcelが吐きだされます。

<事前準備>
    Python3.Xをインストールすること。
    ライブラリをインストールすること。
        ・selenium
        ・subprocess
        ・pandas
        ・re 
        ・datetime

    プログラムと同じディレクトリにChromeDriver.exeを設置すること。

def　関数化するのはどこにしようか
ちいさい粒度でつくる(簡単にする)
緒方のプログラムをみて真似をできる粒度にする。
    →なにやってるかわかるプログラムにする
    →可読性
    →複雑な部分の書き換え
    yamlに書き出す。プログラム、url、保存先(ファイル名はそのままで)
    
Celonis
    sql、pqlができればうごく。→あとはGUI
    pythonを使うとか、OSに近いところはそんなに触ってない。
    ビジネスプロセス

インストール
    手順書(python環境構築、wsl2で動かす。)

    今怖いなぁぽいんと
        現状動かしているのはLinuxPythonだった。
        WinPyとLinPyの競合
        WinPyとLinPyの文字コードが違う、

wsl2を入れてみる。

初期化するときのスクリプト
    現状使っているプログラムに

    バージョン調べる発信 緒方タスク

