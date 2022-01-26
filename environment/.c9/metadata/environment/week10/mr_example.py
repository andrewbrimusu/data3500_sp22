{"changed":true,"filter":false,"title":"mr_example.py","tooltip":"/week10/mr_example.py","value":"import json\n\n# this example from week 7 has been updated to give an example of adding shorting logic\n# please watch week14 zoom session2 for information on how to do this\n\n# note: I named my variable \"short\", \"sell\" would be another great variable name you might want to use\n\n        \ndef meanReversionStrategy(prices):\n    i = 0\n    buy = 0\n    short = 0\n    total_profit = 0\n    for p in prices:\n        if i >= 5: \n            moving_average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5\n            \n            #simple moving average logic, not mean\n            if p < moving_average * .96 and buy == 0: #buy\n                print(\"buying at: \", p)\n                buy = p\n                if short != 0 and buy != 0:\n                    total_profit += short - buy\n                    print(\"trade profit\", short - buy)\n                    print(\"total profit: \", total_profit)\n                short = 0\n            elif p > moving_average * 1.04 and short == 0: #sell, a sell signal is the same thing as a short signal\n                short = p\n                print(\"shorting at: \", p)\n                if short != 0 and buy != 0:\n                    total_profit += short - buy\n                    print(\"trade profit\", short - buy)\n                    print(\"total profit: \", total_profit)\n                buy = 0\n        i += 1\n        \n    final_percentage = (total_profit / prices[0]) * 100\n    print(\"total profit: \", total_profit)\n    print(\"final percentage: \", final_percentage, \"%\")\n    \n    return total_profit, final_percentage\n\n\n\nticker = \"aapl\"\n\nfil = open(\"/home/ubuntu/environment/week10/data/\" + ticker + \".txt\")\nlines = fil.readlines()\n# print(lines)\n\nprices = []\nfor line in lines:\n    prices.append(float(line))      \n    \nprofit, returns = meanReversionStrategy(prices)\n\nprint(ticker, \"profit: \", profit)\nprint(ticker, \"returns: \", returns)\n\nappend_date()\nfor ticker in tickers:\n    # load ticker prices from csv\n    ret, profit = meanReversionStrategy(prices)\n    ","undoManager":{"mark":65,"position":100,"stack":[[{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"remove","lines":[" "],"id":432},{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"remove","lines":["<"]}],[{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":[">"],"id":433}],[{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":[" "],"id":434}],[{"start":{"row":25,"column":36},"end":{"row":25,"column":37},"action":"insert","lines":["*"],"id":435}],[{"start":{"row":25,"column":37},"end":{"row":25,"column":38},"action":"insert","lines":[" "],"id":436},{"start":{"row":25,"column":38},"end":{"row":25,"column":39},"action":"insert","lines":["1"]},{"start":{"row":25,"column":39},"end":{"row":25,"column":40},"action":"insert","lines":["."]},{"start":{"row":25,"column":40},"end":{"row":25,"column":41},"action":"insert","lines":["0"]},{"start":{"row":25,"column":41},"end":{"row":25,"column":42},"action":"insert","lines":["5"]}],[{"start":{"row":25,"column":42},"end":{"row":25,"column":43},"action":"insert","lines":[" "],"id":437}],[{"start":{"row":53,"column":18},"end":{"row":53,"column":45},"action":"remove","lines":["simpleMovingAverageStrategy"],"id":438},{"start":{"row":53,"column":18},"end":{"row":53,"column":39},"action":"insert","lines":["meanReversionStrategy"]}],[{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"remove","lines":["5"],"id":439}],[{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":["6"],"id":440}],[{"start":{"row":25,"column":41},"end":{"row":25,"column":42},"action":"remove","lines":["5"],"id":441}],[{"start":{"row":25,"column":41},"end":{"row":25,"column":42},"action":"insert","lines":["4"],"id":442}],[{"start":{"row":25,"column":64},"end":{"row":25,"column":65},"action":"insert","lines":[" "],"id":443},{"start":{"row":25,"column":65},"end":{"row":25,"column":66},"action":"insert","lines":["9"]}],[{"start":{"row":25,"column":65},"end":{"row":25,"column":66},"action":"remove","lines":["9"],"id":444}],[{"start":{"row":25,"column":65},"end":{"row":25,"column":67},"action":"insert","lines":["()"],"id":445}],[{"start":{"row":25,"column":66},"end":{"row":25,"column":67},"action":"insert","lines":["s"],"id":446},{"start":{"row":25,"column":67},"end":{"row":25,"column":68},"action":"insert","lines":["a"]},{"start":{"row":25,"column":68},"end":{"row":25,"column":69},"action":"insert","lines":["m"]},{"start":{"row":25,"column":69},"end":{"row":25,"column":70},"action":"insert","lines":["e"]}],[{"start":{"row":25,"column":70},"end":{"row":25,"column":71},"action":"insert","lines":[" "],"id":447},{"start":{"row":25,"column":71},"end":{"row":25,"column":72},"action":"insert","lines":["a"]},{"start":{"row":25,"column":72},"end":{"row":25,"column":73},"action":"insert","lines":["s"]}],[{"start":{"row":25,"column":73},"end":{"row":25,"column":74},"action":"insert","lines":[" "],"id":448},{"start":{"row":25,"column":74},"end":{"row":25,"column":75},"action":"insert","lines":["s"]},{"start":{"row":25,"column":75},"end":{"row":25,"column":76},"action":"insert","lines":["h"]},{"start":{"row":25,"column":76},"end":{"row":25,"column":77},"action":"insert","lines":["o"]},{"start":{"row":25,"column":77},"end":{"row":25,"column":78},"action":"insert","lines":["r"]},{"start":{"row":25,"column":78},"end":{"row":25,"column":79},"action":"insert","lines":["t"]},{"start":{"row":25,"column":79},"end":{"row":25,"column":80},"action":"insert","lines":["i"]},{"start":{"row":25,"column":80},"end":{"row":25,"column":81},"action":"insert","lines":["n"]},{"start":{"row":25,"column":81},"end":{"row":25,"column":82},"action":"insert","lines":["g"]}],[{"start":{"row":25,"column":81},"end":{"row":25,"column":82},"action":"remove","lines":["g"],"id":449},{"start":{"row":25,"column":80},"end":{"row":25,"column":81},"action":"remove","lines":["n"]},{"start":{"row":25,"column":79},"end":{"row":25,"column":80},"action":"remove","lines":["i"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["#"],"id":450}],[{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":[" "],"id":451},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["n"]},{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["o"]},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["t"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["e"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":[":"]}],[{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":[" "],"id":452},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["I"]}],[{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":[" "],"id":453},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["n"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["a"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["m"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["e"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":[" "],"id":454},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["m"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["y"]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":[" "],"id":455},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["v"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["a"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["r"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["i"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["a"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["b"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":["l"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":[" "],"id":456}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":30},"action":"insert","lines":["\"\""],"id":457}],[{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"insert","lines":["s"],"id":458},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"insert","lines":["h"]},{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"insert","lines":["o"]},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":["r"]},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"insert","lines":[","],"id":459}],[{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"insert","lines":[" "],"id":460}],[{"start":{"row":5,"column":37},"end":{"row":5,"column":39},"action":"insert","lines":["\"\""],"id":461}],[{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"insert","lines":["s"],"id":462},{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"insert","lines":["e"]},{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"insert","lines":["l"]},{"start":{"row":5,"column":41},"end":{"row":5,"column":42},"action":"insert","lines":["l"]}],[{"start":{"row":5,"column":43},"end":{"row":5,"column":44},"action":"insert","lines":[" "],"id":463},{"start":{"row":5,"column":44},"end":{"row":5,"column":45},"action":"insert","lines":["w"]}],[{"start":{"row":5,"column":44},"end":{"row":5,"column":45},"action":"remove","lines":["w"],"id":464}],[{"start":{"row":5,"column":44},"end":{"row":5,"column":45},"action":"insert","lines":["w"],"id":465},{"start":{"row":5,"column":45},"end":{"row":5,"column":46},"action":"insert","lines":["o"]},{"start":{"row":5,"column":46},"end":{"row":5,"column":47},"action":"insert","lines":["u"]},{"start":{"row":5,"column":47},"end":{"row":5,"column":48},"action":"insert","lines":["l"]},{"start":{"row":5,"column":48},"end":{"row":5,"column":49},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":49},"end":{"row":5,"column":50},"action":"insert","lines":[" "],"id":466},{"start":{"row":5,"column":50},"end":{"row":5,"column":51},"action":"insert","lines":["b"]},{"start":{"row":5,"column":51},"end":{"row":5,"column":52},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":52},"end":{"row":5,"column":53},"action":"insert","lines":[" "],"id":467},{"start":{"row":5,"column":53},"end":{"row":5,"column":54},"action":"insert","lines":["a"]},{"start":{"row":5,"column":54},"end":{"row":5,"column":55},"action":"insert","lines":["n"]},{"start":{"row":5,"column":55},"end":{"row":5,"column":56},"action":"insert","lines":["o"]},{"start":{"row":5,"column":56},"end":{"row":5,"column":57},"action":"insert","lines":["t"]},{"start":{"row":5,"column":57},"end":{"row":5,"column":58},"action":"insert","lines":["h"]},{"start":{"row":5,"column":58},"end":{"row":5,"column":59},"action":"insert","lines":["e"]},{"start":{"row":5,"column":59},"end":{"row":5,"column":60},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":60},"end":{"row":5,"column":61},"action":"insert","lines":[" "],"id":468},{"start":{"row":5,"column":61},"end":{"row":5,"column":62},"action":"insert","lines":["g"]},{"start":{"row":5,"column":62},"end":{"row":5,"column":63},"action":"insert","lines":["r"]},{"start":{"row":5,"column":63},"end":{"row":5,"column":64},"action":"insert","lines":["e"]},{"start":{"row":5,"column":64},"end":{"row":5,"column":65},"action":"insert","lines":["a"]},{"start":{"row":5,"column":65},"end":{"row":5,"column":66},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":66},"end":{"row":5,"column":67},"action":"insert","lines":[" "],"id":469},{"start":{"row":5,"column":67},"end":{"row":5,"column":68},"action":"insert","lines":["v"]},{"start":{"row":5,"column":68},"end":{"row":5,"column":69},"action":"insert","lines":["a"]},{"start":{"row":5,"column":69},"end":{"row":5,"column":70},"action":"insert","lines":["r"]},{"start":{"row":5,"column":70},"end":{"row":5,"column":71},"action":"insert","lines":["i"]},{"start":{"row":5,"column":71},"end":{"row":5,"column":72},"action":"insert","lines":["a"]},{"start":{"row":5,"column":72},"end":{"row":5,"column":73},"action":"insert","lines":["b"]},{"start":{"row":5,"column":73},"end":{"row":5,"column":74},"action":"insert","lines":["l"]},{"start":{"row":5,"column":74},"end":{"row":5,"column":75},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":75},"end":{"row":5,"column":76},"action":"insert","lines":[" "],"id":470},{"start":{"row":5,"column":76},"end":{"row":5,"column":77},"action":"insert","lines":["n"]},{"start":{"row":5,"column":77},"end":{"row":5,"column":78},"action":"insert","lines":["a"]},{"start":{"row":5,"column":78},"end":{"row":5,"column":79},"action":"insert","lines":["m"]},{"start":{"row":5,"column":79},"end":{"row":5,"column":80},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":80},"end":{"row":5,"column":81},"action":"insert","lines":[" "],"id":471},{"start":{"row":5,"column":81},"end":{"row":5,"column":82},"action":"insert","lines":["y"]},{"start":{"row":5,"column":82},"end":{"row":5,"column":83},"action":"insert","lines":["o"]},{"start":{"row":5,"column":83},"end":{"row":5,"column":84},"action":"insert","lines":["u"]}],[{"start":{"row":5,"column":84},"end":{"row":5,"column":85},"action":"insert","lines":[" "],"id":472},{"start":{"row":5,"column":85},"end":{"row":5,"column":86},"action":"insert","lines":["m"]},{"start":{"row":5,"column":86},"end":{"row":5,"column":87},"action":"insert","lines":["g"]},{"start":{"row":5,"column":87},"end":{"row":5,"column":88},"action":"insert","lines":["h"]},{"start":{"row":5,"column":88},"end":{"row":5,"column":89},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":88},"end":{"row":5,"column":89},"action":"remove","lines":["t"],"id":473},{"start":{"row":5,"column":87},"end":{"row":5,"column":88},"action":"remove","lines":["h"]}],[{"start":{"row":5,"column":87},"end":{"row":5,"column":88},"action":"insert","lines":["i"],"id":474},{"start":{"row":5,"column":88},"end":{"row":5,"column":89},"action":"insert","lines":["g"]},{"start":{"row":5,"column":89},"end":{"row":5,"column":90},"action":"insert","lines":["h"]},{"start":{"row":5,"column":90},"end":{"row":5,"column":91},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":90},"end":{"row":5,"column":91},"action":"remove","lines":["t"],"id":475},{"start":{"row":5,"column":89},"end":{"row":5,"column":90},"action":"remove","lines":["h"]},{"start":{"row":5,"column":88},"end":{"row":5,"column":89},"action":"remove","lines":["g"]},{"start":{"row":5,"column":87},"end":{"row":5,"column":88},"action":"remove","lines":["i"]},{"start":{"row":5,"column":86},"end":{"row":5,"column":87},"action":"remove","lines":["g"]}],[{"start":{"row":5,"column":86},"end":{"row":5,"column":87},"action":"insert","lines":["i"],"id":476},{"start":{"row":5,"column":87},"end":{"row":5,"column":88},"action":"insert","lines":["g"]},{"start":{"row":5,"column":88},"end":{"row":5,"column":89},"action":"insert","lines":["h"]},{"start":{"row":5,"column":89},"end":{"row":5,"column":90},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":90},"end":{"row":5,"column":91},"action":"insert","lines":[" "],"id":477},{"start":{"row":5,"column":91},"end":{"row":5,"column":92},"action":"insert","lines":["w"]},{"start":{"row":5,"column":92},"end":{"row":5,"column":93},"action":"insert","lines":["a"]},{"start":{"row":5,"column":93},"end":{"row":5,"column":94},"action":"insert","lines":["n"]},{"start":{"row":5,"column":94},"end":{"row":5,"column":95},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":95},"end":{"row":5,"column":96},"action":"insert","lines":[" "],"id":478},{"start":{"row":5,"column":96},"end":{"row":5,"column":97},"action":"insert","lines":["t"]},{"start":{"row":5,"column":97},"end":{"row":5,"column":98},"action":"insert","lines":["o"]}],[{"start":{"row":5,"column":98},"end":{"row":5,"column":99},"action":"insert","lines":[" "],"id":479},{"start":{"row":5,"column":99},"end":{"row":5,"column":100},"action":"insert","lines":["u"]},{"start":{"row":5,"column":100},"end":{"row":5,"column":101},"action":"insert","lines":["s"]},{"start":{"row":5,"column":101},"end":{"row":5,"column":102},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":102},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":480}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":23},"action":"insert","lines":["/week10/mva5_inclass.py"],"id":481}],[{"start":{"row":27,"column":16},"end":{"row":27,"column":21},"action":"remove","lines":["short"],"id":482},{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["f"]},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["o"]},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":["o"]},{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":["b"]},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["a"]},{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"insert","lines":["r"]}],[{"start":{"row":27,"column":16},"end":{"row":27,"column":22},"action":"remove","lines":["foobar"],"id":483},{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["s"]},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["h"]},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":["o"]},{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":["r"]},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"remove","lines":["#"],"id":484}],[{"start":{"row":26,"column":65},"end":{"row":26,"column":80},"action":"remove","lines":["(same as short)"],"id":486},{"start":{"row":26,"column":64},"end":{"row":26,"column":65},"action":"remove","lines":[" "]}],[{"start":{"row":26,"column":64},"end":{"row":26,"column":65},"action":"insert","lines":[","],"id":487}],[{"start":{"row":26,"column":65},"end":{"row":26,"column":66},"action":"insert","lines":[" "],"id":488},{"start":{"row":26,"column":66},"end":{"row":26,"column":67},"action":"insert","lines":["a"]}],[{"start":{"row":26,"column":67},"end":{"row":26,"column":68},"action":"insert","lines":[" "],"id":489},{"start":{"row":26,"column":68},"end":{"row":26,"column":69},"action":"insert","lines":["s"]},{"start":{"row":26,"column":69},"end":{"row":26,"column":70},"action":"insert","lines":["e"]},{"start":{"row":26,"column":70},"end":{"row":26,"column":71},"action":"insert","lines":["l"]},{"start":{"row":26,"column":71},"end":{"row":26,"column":72},"action":"insert","lines":["l"]}],[{"start":{"row":26,"column":72},"end":{"row":26,"column":73},"action":"insert","lines":[" "],"id":490},{"start":{"row":26,"column":73},"end":{"row":26,"column":74},"action":"insert","lines":["s"]},{"start":{"row":26,"column":74},"end":{"row":26,"column":75},"action":"insert","lines":["i"]},{"start":{"row":26,"column":75},"end":{"row":26,"column":76},"action":"insert","lines":["g"]},{"start":{"row":26,"column":76},"end":{"row":26,"column":77},"action":"insert","lines":["n"]},{"start":{"row":26,"column":77},"end":{"row":26,"column":78},"action":"insert","lines":["a"]},{"start":{"row":26,"column":78},"end":{"row":26,"column":79},"action":"insert","lines":["l"]}],[{"start":{"row":26,"column":79},"end":{"row":26,"column":80},"action":"insert","lines":[" "],"id":491},{"start":{"row":26,"column":80},"end":{"row":26,"column":81},"action":"insert","lines":["i"]},{"start":{"row":26,"column":81},"end":{"row":26,"column":82},"action":"insert","lines":["s"]}],[{"start":{"row":26,"column":82},"end":{"row":26,"column":83},"action":"insert","lines":[" "],"id":492},{"start":{"row":26,"column":83},"end":{"row":26,"column":84},"action":"insert","lines":["t"]},{"start":{"row":26,"column":84},"end":{"row":26,"column":85},"action":"insert","lines":["h"]},{"start":{"row":26,"column":85},"end":{"row":26,"column":86},"action":"insert","lines":["e"]}],[{"start":{"row":26,"column":86},"end":{"row":26,"column":87},"action":"insert","lines":[" "],"id":493},{"start":{"row":26,"column":87},"end":{"row":26,"column":88},"action":"insert","lines":["s"]},{"start":{"row":26,"column":88},"end":{"row":26,"column":89},"action":"insert","lines":["a"]},{"start":{"row":26,"column":89},"end":{"row":26,"column":90},"action":"insert","lines":["m"]},{"start":{"row":26,"column":90},"end":{"row":26,"column":91},"action":"insert","lines":["e"]}],[{"start":{"row":26,"column":91},"end":{"row":26,"column":92},"action":"insert","lines":[" "],"id":494},{"start":{"row":26,"column":92},"end":{"row":26,"column":93},"action":"insert","lines":["t"]},{"start":{"row":26,"column":93},"end":{"row":26,"column":94},"action":"insert","lines":["h"]},{"start":{"row":26,"column":94},"end":{"row":26,"column":95},"action":"insert","lines":["i"]},{"start":{"row":26,"column":95},"end":{"row":26,"column":96},"action":"insert","lines":["n"]},{"start":{"row":26,"column":96},"end":{"row":26,"column":97},"action":"insert","lines":["g"]}],[{"start":{"row":26,"column":97},"end":{"row":26,"column":98},"action":"insert","lines":[" "],"id":495},{"start":{"row":26,"column":98},"end":{"row":26,"column":99},"action":"insert","lines":["a"]},{"start":{"row":26,"column":99},"end":{"row":26,"column":100},"action":"insert","lines":["s"]}],[{"start":{"row":26,"column":100},"end":{"row":26,"column":101},"action":"insert","lines":[" "],"id":496},{"start":{"row":26,"column":101},"end":{"row":26,"column":102},"action":"insert","lines":["a"]}],[{"start":{"row":26,"column":102},"end":{"row":26,"column":103},"action":"insert","lines":[" "],"id":497},{"start":{"row":26,"column":103},"end":{"row":26,"column":104},"action":"insert","lines":["s"]},{"start":{"row":26,"column":104},"end":{"row":26,"column":105},"action":"insert","lines":["h"]},{"start":{"row":26,"column":105},"end":{"row":26,"column":106},"action":"insert","lines":["o"]},{"start":{"row":26,"column":106},"end":{"row":26,"column":107},"action":"insert","lines":["r"]},{"start":{"row":26,"column":107},"end":{"row":26,"column":108},"action":"insert","lines":["t"]}],[{"start":{"row":26,"column":108},"end":{"row":26,"column":109},"action":"insert","lines":[" "],"id":498},{"start":{"row":26,"column":109},"end":{"row":26,"column":110},"action":"insert","lines":["s"]},{"start":{"row":26,"column":110},"end":{"row":26,"column":111},"action":"insert","lines":["i"]},{"start":{"row":26,"column":111},"end":{"row":26,"column":112},"action":"insert","lines":["g"]},{"start":{"row":26,"column":112},"end":{"row":26,"column":113},"action":"insert","lines":["n"]},{"start":{"row":26,"column":113},"end":{"row":26,"column":114},"action":"insert","lines":["a"]},{"start":{"row":26,"column":114},"end":{"row":26,"column":115},"action":"insert","lines":["l"]}],[{"start":{"row":58,"column":0},"end":{"row":59,"column":0},"action":"insert","lines":["",""],"id":499},{"start":{"row":59,"column":0},"end":{"row":60,"column":0},"action":"insert","lines":["",""]},{"start":{"row":60,"column":0},"end":{"row":60,"column":1},"action":"insert","lines":["f"]},{"start":{"row":60,"column":1},"end":{"row":60,"column":2},"action":"insert","lines":["o"]},{"start":{"row":60,"column":2},"end":{"row":60,"column":3},"action":"insert","lines":["r"]}],[{"start":{"row":60,"column":3},"end":{"row":60,"column":4},"action":"insert","lines":[" "],"id":500},{"start":{"row":60,"column":4},"end":{"row":60,"column":5},"action":"insert","lines":["t"]},{"start":{"row":60,"column":5},"end":{"row":60,"column":6},"action":"insert","lines":["i"]},{"start":{"row":60,"column":6},"end":{"row":60,"column":7},"action":"insert","lines":["c"]},{"start":{"row":60,"column":7},"end":{"row":60,"column":8},"action":"insert","lines":["k"]},{"start":{"row":60,"column":8},"end":{"row":60,"column":9},"action":"insert","lines":["e"]},{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"insert","lines":["r"]}],[{"start":{"row":60,"column":10},"end":{"row":60,"column":11},"action":"insert","lines":[" "],"id":501},{"start":{"row":60,"column":11},"end":{"row":60,"column":12},"action":"insert","lines":["i"]},{"start":{"row":60,"column":12},"end":{"row":60,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":60,"column":13},"end":{"row":60,"column":14},"action":"insert","lines":[" "],"id":502},{"start":{"row":60,"column":14},"end":{"row":60,"column":15},"action":"insert","lines":["t"]},{"start":{"row":60,"column":15},"end":{"row":60,"column":16},"action":"insert","lines":["i"]},{"start":{"row":60,"column":16},"end":{"row":60,"column":17},"action":"insert","lines":["c"]},{"start":{"row":60,"column":17},"end":{"row":60,"column":18},"action":"insert","lines":["k"]},{"start":{"row":60,"column":18},"end":{"row":60,"column":19},"action":"insert","lines":["r"]},{"start":{"row":60,"column":19},"end":{"row":60,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":60,"column":19},"end":{"row":60,"column":20},"action":"remove","lines":["r"],"id":503},{"start":{"row":60,"column":18},"end":{"row":60,"column":19},"action":"remove","lines":["r"]}],[{"start":{"row":60,"column":18},"end":{"row":60,"column":19},"action":"insert","lines":["e"],"id":504},{"start":{"row":60,"column":19},"end":{"row":60,"column":20},"action":"insert","lines":["r"]},{"start":{"row":60,"column":20},"end":{"row":60,"column":21},"action":"insert","lines":["s"]},{"start":{"row":60,"column":21},"end":{"row":60,"column":22},"action":"insert","lines":[":"]}],[{"start":{"row":60,"column":22},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":505},{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":59,"column":0},"end":{"row":59,"column":1},"action":"insert","lines":["a"],"id":506},{"start":{"row":59,"column":1},"end":{"row":59,"column":2},"action":"insert","lines":["p"]},{"start":{"row":59,"column":2},"end":{"row":59,"column":3},"action":"insert","lines":["p"]},{"start":{"row":59,"column":3},"end":{"row":59,"column":4},"action":"insert","lines":["e"]},{"start":{"row":59,"column":4},"end":{"row":59,"column":5},"action":"insert","lines":["n"]},{"start":{"row":59,"column":5},"end":{"row":59,"column":6},"action":"insert","lines":["d"]}],[{"start":{"row":59,"column":6},"end":{"row":59,"column":8},"action":"insert","lines":["()"],"id":507}],[{"start":{"row":59,"column":7},"end":{"row":59,"column":8},"action":"insert","lines":["d"],"id":508},{"start":{"row":59,"column":8},"end":{"row":59,"column":9},"action":"insert","lines":["a"]},{"start":{"row":59,"column":9},"end":{"row":59,"column":10},"action":"insert","lines":["t"]},{"start":{"row":59,"column":10},"end":{"row":59,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":59,"column":10},"end":{"row":59,"column":11},"action":"remove","lines":["e"],"id":509},{"start":{"row":59,"column":9},"end":{"row":59,"column":10},"action":"remove","lines":["t"]},{"start":{"row":59,"column":8},"end":{"row":59,"column":9},"action":"remove","lines":["a"]},{"start":{"row":59,"column":7},"end":{"row":59,"column":8},"action":"remove","lines":["d"]},{"start":{"row":59,"column":6},"end":{"row":59,"column":8},"action":"remove","lines":["()"]}],[{"start":{"row":59,"column":6},"end":{"row":59,"column":7},"action":"insert","lines":["_"],"id":510},{"start":{"row":59,"column":7},"end":{"row":59,"column":8},"action":"insert","lines":["d"]},{"start":{"row":59,"column":8},"end":{"row":59,"column":9},"action":"insert","lines":["a"]},{"start":{"row":59,"column":9},"end":{"row":59,"column":10},"action":"insert","lines":["t"]},{"start":{"row":59,"column":10},"end":{"row":59,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":59,"column":11},"end":{"row":59,"column":13},"action":"insert","lines":["()"],"id":511}],[{"start":{"row":61,"column":4},"end":{"row":61,"column":5},"action":"insert","lines":["#"],"id":512}],[{"start":{"row":61,"column":5},"end":{"row":61,"column":6},"action":"insert","lines":[" "],"id":513},{"start":{"row":61,"column":6},"end":{"row":61,"column":7},"action":"insert","lines":["l"]},{"start":{"row":61,"column":7},"end":{"row":61,"column":8},"action":"insert","lines":["o"]},{"start":{"row":61,"column":8},"end":{"row":61,"column":9},"action":"insert","lines":["a"]},{"start":{"row":61,"column":9},"end":{"row":61,"column":10},"action":"insert","lines":["d"]}],[{"start":{"row":61,"column":10},"end":{"row":61,"column":11},"action":"insert","lines":[" "],"id":514},{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"insert","lines":["t"]},{"start":{"row":61,"column":12},"end":{"row":61,"column":13},"action":"insert","lines":["i"]},{"start":{"row":61,"column":13},"end":{"row":61,"column":14},"action":"insert","lines":["c"]},{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"insert","lines":["k"]},{"start":{"row":61,"column":15},"end":{"row":61,"column":16},"action":"insert","lines":["e"]},{"start":{"row":61,"column":16},"end":{"row":61,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":61,"column":17},"end":{"row":61,"column":18},"action":"insert","lines":[" "],"id":515},{"start":{"row":61,"column":18},"end":{"row":61,"column":19},"action":"insert","lines":["p"]},{"start":{"row":61,"column":19},"end":{"row":61,"column":20},"action":"insert","lines":["r"]},{"start":{"row":61,"column":20},"end":{"row":61,"column":21},"action":"insert","lines":["i"]},{"start":{"row":61,"column":21},"end":{"row":61,"column":22},"action":"insert","lines":["c"]},{"start":{"row":61,"column":22},"end":{"row":61,"column":23},"action":"insert","lines":["e"]},{"start":{"row":61,"column":23},"end":{"row":61,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":61,"column":24},"end":{"row":61,"column":25},"action":"insert","lines":[" "],"id":516},{"start":{"row":61,"column":25},"end":{"row":61,"column":26},"action":"insert","lines":["f"]},{"start":{"row":61,"column":26},"end":{"row":61,"column":27},"action":"insert","lines":["r"]},{"start":{"row":61,"column":27},"end":{"row":61,"column":28},"action":"insert","lines":["o"]},{"start":{"row":61,"column":28},"end":{"row":61,"column":29},"action":"insert","lines":["m"]}],[{"start":{"row":61,"column":29},"end":{"row":61,"column":30},"action":"insert","lines":[" "],"id":517},{"start":{"row":61,"column":30},"end":{"row":61,"column":31},"action":"insert","lines":["c"]},{"start":{"row":61,"column":31},"end":{"row":61,"column":32},"action":"insert","lines":["s"]},{"start":{"row":61,"column":32},"end":{"row":61,"column":33},"action":"insert","lines":["x"]},{"start":{"row":61,"column":33},"end":{"row":61,"column":34},"action":"insert","lines":["v"]}],[{"start":{"row":61,"column":33},"end":{"row":61,"column":34},"action":"remove","lines":["v"],"id":518},{"start":{"row":61,"column":32},"end":{"row":61,"column":33},"action":"remove","lines":["x"]}],[{"start":{"row":61,"column":32},"end":{"row":61,"column":33},"action":"insert","lines":["v"],"id":519}],[{"start":{"row":61,"column":33},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":520},{"start":{"row":62,"column":0},"end":{"row":62,"column":4},"action":"insert","lines":["    "]},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"insert","lines":["R"]},{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"insert","lines":["E"]},{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"insert","lines":["T"]}],[{"start":{"row":62,"column":7},"end":{"row":62,"column":8},"action":"insert","lines":[" "],"id":521}],[{"start":{"row":62,"column":7},"end":{"row":62,"column":8},"action":"remove","lines":[" "],"id":522},{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"remove","lines":["T"]},{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"remove","lines":["E"]},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"remove","lines":["R"]}],[{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"insert","lines":["r"],"id":523},{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"insert","lines":["w"]},{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"remove","lines":["e"],"id":524},{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"remove","lines":["w"]}],[{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"insert","lines":["e"],"id":525},{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"insert","lines":["t"]},{"start":{"row":62,"column":7},"end":{"row":62,"column":8},"action":"insert","lines":[","]}],[{"start":{"row":62,"column":8},"end":{"row":62,"column":9},"action":"insert","lines":[" "],"id":526},{"start":{"row":62,"column":9},"end":{"row":62,"column":10},"action":"insert","lines":["p"]},{"start":{"row":62,"column":10},"end":{"row":62,"column":11},"action":"insert","lines":["r"]},{"start":{"row":62,"column":11},"end":{"row":62,"column":12},"action":"insert","lines":["o"]},{"start":{"row":62,"column":12},"end":{"row":62,"column":13},"action":"insert","lines":["f"]},{"start":{"row":62,"column":13},"end":{"row":62,"column":14},"action":"insert","lines":["i"]},{"start":{"row":62,"column":14},"end":{"row":62,"column":15},"action":"insert","lines":["t"]},{"start":{"row":62,"column":15},"end":{"row":62,"column":16},"action":"insert","lines":[","]}],[{"start":{"row":62,"column":16},"end":{"row":62,"column":17},"action":"insert","lines":[" "],"id":527}],[{"start":{"row":62,"column":16},"end":{"row":62,"column":17},"action":"remove","lines":[" "],"id":528},{"start":{"row":62,"column":15},"end":{"row":62,"column":16},"action":"remove","lines":[","]}],[{"start":{"row":62,"column":15},"end":{"row":62,"column":16},"action":"insert","lines":[" "],"id":529},{"start":{"row":62,"column":16},"end":{"row":62,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":62,"column":17},"end":{"row":62,"column":18},"action":"insert","lines":[" "],"id":530},{"start":{"row":62,"column":18},"end":{"row":62,"column":19},"action":"insert","lines":["m"]},{"start":{"row":62,"column":19},"end":{"row":62,"column":20},"action":"insert","lines":["e"]},{"start":{"row":62,"column":20},"end":{"row":62,"column":21},"action":"insert","lines":["a"]},{"start":{"row":62,"column":21},"end":{"row":62,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":62,"column":18},"end":{"row":62,"column":22},"action":"remove","lines":["mean"],"id":531},{"start":{"row":62,"column":18},"end":{"row":62,"column":41},"action":"insert","lines":["meanReversionStrategy()"]}],[{"start":{"row":62,"column":40},"end":{"row":62,"column":41},"action":"insert","lines":["p"],"id":532},{"start":{"row":62,"column":41},"end":{"row":62,"column":42},"action":"insert","lines":["r"]},{"start":{"row":62,"column":42},"end":{"row":62,"column":43},"action":"insert","lines":["i"]},{"start":{"row":62,"column":43},"end":{"row":62,"column":44},"action":"insert","lines":["c"]},{"start":{"row":62,"column":44},"end":{"row":62,"column":45},"action":"insert","lines":["e"]},{"start":{"row":62,"column":45},"end":{"row":62,"column":46},"action":"insert","lines":["s"]}],[{"start":{"row":62,"column":47},"end":{"row":63,"column":0},"action":"insert","lines":["",""],"id":533},{"start":{"row":63,"column":0},"end":{"row":63,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":421,"scrollleft":0,"selection":{"start":{"row":55,"column":0},"end":{"row":55,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1638808379199}