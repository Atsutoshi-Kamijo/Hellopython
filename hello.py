indxs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fname_tmpl = 'data.%02d'
for i in indxs:
    fname = fname_tmpl % i
    print(fname)          # ためしに fname を表示させてみる．
    # ここに fname を使った処理を書いていく