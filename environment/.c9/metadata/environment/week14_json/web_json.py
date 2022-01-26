{"changed":true,"filter":false,"title":"web_json.py","tooltip":"/week14_json/web_json.py","value":"import requests\nimport json\n    \ndef create_data():\n    tickers = ['AAPL', 'ADBE']\n    for ticker in tickers:\n        url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'\n        print(url)\n        request = requests.get(url)\n        rqst_dict = json.loads(request.text)\n        key_series = \"Time Series (Daily)\"\n        key_open = '1. open'\n        key_close = '4. close'\n        key_hi = '2. high'\n        key_lo = '3. low'\n        \n        prices = []\n        \n        for date in rqst_dict[key_series]:\n            row = \"\"\n            row += date + \",\"\n            row += rqst_dict[key_series][date][key_open] + \",\"\n            row += rqst_dict[key_series][date][key_hi] + \",\"\n            row += rqst_dict[key_series][date][key_lo] + \",\"\n            row += rqst_dict[key_series][date][key_close] + \"\\n\"\n            \n            prices.append(row)\n            \n        prices.reverse()\n        \n        # print(prices)    \n        \n        csv_file = open(ticker + \".csv\", \"w\")\n        csv_file.write(\"date,open,hi,lo,close\\n\")\n        \n        for row in prices:\n            csv_file.write(row)\n            \n        csv_file.close()\n        \n    \n    \n    \ndef append_data():\n    #this function appends new data, hooray!\n    ticker = 'AAPL'\n    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'\n    print(url)\n    request = requests.get(url)\n    rqst_dict = json.loads(request.text)\n    # print(rqst_dict)\n    \n    key_series = \"Time Series (Daily)\"\n    key_open = '1. open'\n    key_close = '4. close'\n    key_hi = '2. high'\n    key_lo = '3. low'\n    \n    # get the last day, of data\n    file = open(ticker + \".csv\")\n    lines = file.readlines()\n    last_line = lines[-1]\n    items = last_line.split(\",\")\n    last_date = items[0]\n    \n    # last_date = open(ticker + \".csv\").readlines()[-1].split(\",\")[0]\n    \n    prices = []\n    \n    for date in rqst_dict[key_series]:\n        row = \"\"\n        row += date + \",\"\n        row += rqst_dict[key_series][date][key_open] + \",\"\n        row += rqst_dict[key_series][date][key_hi] + \",\"\n        row += rqst_dict[key_series][date][key_lo] + \",\"\n        row += rqst_dict[key_series][date][key_close] + \"\\n\"\n        if date > last_date:\n            prices.append(row)\n        \n    prices.reverse()\n    \n    # print(prices)    \n    \n    csv_file = open(ticker + \".csv\", \"a\")\n    \n    for row in prices:\n        csv_file.write(row)\n        \n    csv_file.close()\n    \n\nappend_data()\n    \n","undoManager":{"mark":-2,"position":100,"stack":[[{"start":{"row":61,"column":59},"end":{"row":61,"column":61},"action":"insert","lines":["[]"],"id":22778}],[{"start":{"row":61,"column":60},"end":{"row":61,"column":61},"action":"insert","lines":["0"],"id":22779}],[{"start":{"row":72,"column":8},"end":{"row":72,"column":9},"action":"insert","lines":["i"],"id":22780},{"start":{"row":72,"column":9},"end":{"row":72,"column":10},"action":"insert","lines":["f"]}],[{"start":{"row":72,"column":10},"end":{"row":72,"column":11},"action":"insert","lines":[" "],"id":22781},{"start":{"row":72,"column":11},"end":{"row":72,"column":12},"action":"insert","lines":["d"]},{"start":{"row":72,"column":12},"end":{"row":72,"column":13},"action":"insert","lines":["a"]},{"start":{"row":72,"column":13},"end":{"row":72,"column":14},"action":"insert","lines":["t"]},{"start":{"row":72,"column":14},"end":{"row":72,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":72,"column":15},"end":{"row":72,"column":16},"action":"insert","lines":[" "],"id":22782},{"start":{"row":72,"column":16},"end":{"row":72,"column":17},"action":"insert","lines":[">"]}],[{"start":{"row":72,"column":17},"end":{"row":72,"column":18},"action":"insert","lines":[" "],"id":22783}],[{"start":{"row":61,"column":4},"end":{"row":61,"column":5},"action":"insert","lines":["l"],"id":22784},{"start":{"row":61,"column":5},"end":{"row":61,"column":6},"action":"insert","lines":["a"]},{"start":{"row":61,"column":6},"end":{"row":61,"column":7},"action":"insert","lines":["s"]},{"start":{"row":61,"column":7},"end":{"row":61,"column":8},"action":"insert","lines":["t"]},{"start":{"row":61,"column":8},"end":{"row":61,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":72,"column":18},"end":{"row":72,"column":19},"action":"insert","lines":["l"],"id":22785}],[{"start":{"row":72,"column":18},"end":{"row":72,"column":19},"action":"remove","lines":["l"],"id":22786},{"start":{"row":72,"column":18},"end":{"row":72,"column":27},"action":"insert","lines":["last_date"]}],[{"start":{"row":72,"column":27},"end":{"row":72,"column":28},"action":"insert","lines":[":"],"id":22787}],[{"start":{"row":73,"column":8},"end":{"row":73,"column":12},"action":"insert","lines":["    "],"id":22788}],[{"start":{"row":79,"column":41},"end":{"row":80,"column":45},"action":"remove","lines":["","    csv_file.write(\"date,open,hi,lo,close\\n\")"],"id":22789}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":6},"action":"insert","lines":["# "],"id":22790}],[{"start":{"row":51,"column":22},"end":{"row":52,"column":11},"action":"remove","lines":["","    input()"],"id":22791}],[{"start":{"row":59,"column":31},"end":{"row":60,"column":0},"action":"insert","lines":["",""],"id":22792},{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"insert","lines":["    "]},{"start":{"row":60,"column":4},"end":{"row":60,"column":5},"action":"insert","lines":["f"]},{"start":{"row":60,"column":5},"end":{"row":60,"column":6},"action":"insert","lines":["i"]},{"start":{"row":60,"column":6},"end":{"row":60,"column":7},"action":"insert","lines":["l"]},{"start":{"row":60,"column":7},"end":{"row":60,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":60,"column":8},"end":{"row":60,"column":9},"action":"insert","lines":[" "],"id":22793},{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":60,"column":10},"end":{"row":60,"column":11},"action":"insert","lines":[" "],"id":22794}],[{"start":{"row":60,"column":11},"end":{"row":60,"column":32},"action":"insert","lines":["open(ticker + \".csv\")"],"id":22795}],[{"start":{"row":60,"column":32},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":22796},{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"insert","lines":["    "]},{"start":{"row":61,"column":4},"end":{"row":61,"column":5},"action":"insert","lines":["l"]},{"start":{"row":61,"column":5},"end":{"row":61,"column":6},"action":"insert","lines":["i"]},{"start":{"row":61,"column":6},"end":{"row":61,"column":7},"action":"insert","lines":["n"]},{"start":{"row":61,"column":7},"end":{"row":61,"column":8},"action":"insert","lines":["e"]},{"start":{"row":61,"column":8},"end":{"row":61,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":61,"column":9},"end":{"row":61,"column":10},"action":"insert","lines":[" "],"id":22797},{"start":{"row":61,"column":10},"end":{"row":61,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"insert","lines":[" "],"id":22798},{"start":{"row":61,"column":12},"end":{"row":61,"column":13},"action":"insert","lines":["f"]},{"start":{"row":61,"column":13},"end":{"row":61,"column":14},"action":"insert","lines":["i"]},{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"insert","lines":["l"]},{"start":{"row":61,"column":15},"end":{"row":61,"column":16},"action":"insert","lines":["e"]},{"start":{"row":61,"column":16},"end":{"row":61,"column":17},"action":"insert","lines":["."]},{"start":{"row":61,"column":17},"end":{"row":61,"column":18},"action":"insert","lines":["r"]}],[{"start":{"row":61,"column":18},"end":{"row":61,"column":19},"action":"insert","lines":["e"],"id":22799},{"start":{"row":61,"column":19},"end":{"row":61,"column":20},"action":"insert","lines":["a"]},{"start":{"row":61,"column":20},"end":{"row":61,"column":21},"action":"insert","lines":["d"]},{"start":{"row":61,"column":21},"end":{"row":61,"column":22},"action":"insert","lines":["l"]},{"start":{"row":61,"column":22},"end":{"row":61,"column":23},"action":"insert","lines":["i"]},{"start":{"row":61,"column":23},"end":{"row":61,"column":24},"action":"insert","lines":["n"]},{"start":{"row":61,"column":24},"end":{"row":61,"column":25},"action":"insert","lines":["e"]},{"start":{"row":61,"column":25},"end":{"row":61,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":61,"column":26},"end":{"row":61,"column":28},"action":"insert","lines":["()"],"id":22800}],[{"start":{"row":61,"column":28},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":22801},{"start":{"row":62,"column":0},"end":{"row":62,"column":4},"action":"insert","lines":["    "]},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"insert","lines":["l"]},{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"insert","lines":["a"]},{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"insert","lines":["s"]},{"start":{"row":62,"column":7},"end":{"row":62,"column":8},"action":"insert","lines":["t"]},{"start":{"row":62,"column":8},"end":{"row":62,"column":9},"action":"insert","lines":["_"]},{"start":{"row":62,"column":9},"end":{"row":62,"column":10},"action":"insert","lines":["l"]},{"start":{"row":62,"column":10},"end":{"row":62,"column":11},"action":"insert","lines":["i"]},{"start":{"row":62,"column":11},"end":{"row":62,"column":12},"action":"insert","lines":["n"]},{"start":{"row":62,"column":12},"end":{"row":62,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":62,"column":13},"end":{"row":62,"column":14},"action":"insert","lines":[" "],"id":22802},{"start":{"row":62,"column":14},"end":{"row":62,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":62,"column":15},"end":{"row":62,"column":16},"action":"insert","lines":[" "],"id":22803},{"start":{"row":62,"column":16},"end":{"row":62,"column":17},"action":"insert","lines":["l"]},{"start":{"row":62,"column":17},"end":{"row":62,"column":18},"action":"insert","lines":["i"]},{"start":{"row":62,"column":18},"end":{"row":62,"column":19},"action":"insert","lines":["n"]},{"start":{"row":62,"column":19},"end":{"row":62,"column":20},"action":"insert","lines":["e"]},{"start":{"row":62,"column":20},"end":{"row":62,"column":21},"action":"insert","lines":["s"]}],[{"start":{"row":62,"column":21},"end":{"row":62,"column":23},"action":"insert","lines":["[]"],"id":22804}],[{"start":{"row":62,"column":22},"end":{"row":62,"column":23},"action":"insert","lines":["-"],"id":22805},{"start":{"row":62,"column":23},"end":{"row":62,"column":24},"action":"insert","lines":["1"]}],[{"start":{"row":62,"column":25},"end":{"row":63,"column":0},"action":"insert","lines":["",""],"id":22806},{"start":{"row":63,"column":0},"end":{"row":63,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":63,"column":4},"end":{"row":63,"column":5},"action":"insert","lines":["i"],"id":22807},{"start":{"row":63,"column":5},"end":{"row":63,"column":6},"action":"insert","lines":["t"]},{"start":{"row":63,"column":6},"end":{"row":63,"column":7},"action":"insert","lines":["e"]},{"start":{"row":63,"column":7},"end":{"row":63,"column":8},"action":"insert","lines":["m"]},{"start":{"row":63,"column":8},"end":{"row":63,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":63,"column":9},"end":{"row":63,"column":10},"action":"insert","lines":[" "],"id":22808},{"start":{"row":63,"column":10},"end":{"row":63,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":63,"column":11},"end":{"row":63,"column":12},"action":"insert","lines":[" "],"id":22809},{"start":{"row":63,"column":12},"end":{"row":63,"column":13},"action":"insert","lines":["l"]},{"start":{"row":63,"column":13},"end":{"row":63,"column":14},"action":"insert","lines":["a"]},{"start":{"row":63,"column":14},"end":{"row":63,"column":15},"action":"insert","lines":["s"]},{"start":{"row":63,"column":15},"end":{"row":63,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":63,"column":12},"end":{"row":63,"column":16},"action":"remove","lines":["last"],"id":22810},{"start":{"row":63,"column":12},"end":{"row":63,"column":21},"action":"insert","lines":["last_line"]}],[{"start":{"row":63,"column":21},"end":{"row":63,"column":22},"action":"insert","lines":["."],"id":22811},{"start":{"row":63,"column":22},"end":{"row":63,"column":23},"action":"insert","lines":["s"]},{"start":{"row":63,"column":23},"end":{"row":63,"column":24},"action":"insert","lines":["p"]},{"start":{"row":63,"column":24},"end":{"row":63,"column":25},"action":"insert","lines":["l"]},{"start":{"row":63,"column":25},"end":{"row":63,"column":26},"action":"insert","lines":["i"]},{"start":{"row":63,"column":26},"end":{"row":63,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":63,"column":27},"end":{"row":63,"column":29},"action":"insert","lines":["()"],"id":22812}],[{"start":{"row":63,"column":28},"end":{"row":63,"column":30},"action":"insert","lines":["\"\""],"id":22813}],[{"start":{"row":63,"column":29},"end":{"row":63,"column":30},"action":"insert","lines":[","],"id":22814}],[{"start":{"row":63,"column":32},"end":{"row":64,"column":0},"action":"insert","lines":["",""],"id":22815},{"start":{"row":64,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["    "]},{"start":{"row":64,"column":4},"end":{"row":64,"column":5},"action":"insert","lines":["l"]},{"start":{"row":64,"column":5},"end":{"row":64,"column":6},"action":"insert","lines":["a"]},{"start":{"row":64,"column":6},"end":{"row":64,"column":7},"action":"insert","lines":["s"]},{"start":{"row":64,"column":7},"end":{"row":64,"column":8},"action":"insert","lines":["t"]},{"start":{"row":64,"column":8},"end":{"row":64,"column":9},"action":"insert","lines":["_"]},{"start":{"row":64,"column":9},"end":{"row":64,"column":10},"action":"insert","lines":["d"]},{"start":{"row":64,"column":10},"end":{"row":64,"column":11},"action":"insert","lines":["a"]},{"start":{"row":64,"column":11},"end":{"row":64,"column":12},"action":"insert","lines":["t"]},{"start":{"row":64,"column":12},"end":{"row":64,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":64,"column":13},"end":{"row":64,"column":14},"action":"insert","lines":[" "],"id":22816},{"start":{"row":64,"column":14},"end":{"row":64,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":64,"column":15},"end":{"row":64,"column":16},"action":"insert","lines":[" "],"id":22817},{"start":{"row":64,"column":16},"end":{"row":64,"column":17},"action":"insert","lines":["i"]},{"start":{"row":64,"column":17},"end":{"row":64,"column":18},"action":"insert","lines":["t"]},{"start":{"row":64,"column":18},"end":{"row":64,"column":19},"action":"insert","lines":["e"]},{"start":{"row":64,"column":19},"end":{"row":64,"column":20},"action":"insert","lines":["m"]},{"start":{"row":64,"column":20},"end":{"row":64,"column":21},"action":"insert","lines":["s"]}],[{"start":{"row":64,"column":21},"end":{"row":64,"column":23},"action":"insert","lines":["[]"],"id":22818}],[{"start":{"row":64,"column":22},"end":{"row":64,"column":23},"action":"insert","lines":["0"],"id":22819}],[{"start":{"row":64,"column":23},"end":{"row":65,"column":0},"action":"insert","lines":["",""],"id":22820},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"remove","lines":["    "],"id":22821},{"start":{"row":64,"column":23},"end":{"row":65,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":64,"column":24},"end":{"row":65,"column":0},"action":"insert","lines":["",""],"id":22822},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":66,"column":4},"end":{"row":66,"column":6},"action":"insert","lines":["# "],"id":22823}],[{"start":{"row":4,"column":19},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":22824},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["f"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["o"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":[" "],"id":22825},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["t"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["i"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["c"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["k"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["e"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":[" "],"id":22826},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["i"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":[" "],"id":22827},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["t"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["i"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["c"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["k"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["e"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["r"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["s"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":[":"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "],"id":22828},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":19},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":22829},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["t"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["i"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["c"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["k"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["e"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["r"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":[" "],"id":22830},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":[" "],"id":22831}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":16},"action":"insert","lines":["[]"],"id":22832}],[{"start":{"row":5,"column":15},"end":{"row":5,"column":17},"action":"insert","lines":["''"],"id":22833}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["A"],"id":22834},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["A"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["P"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["L"]}],[{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":[","],"id":22835}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":[" "],"id":22836},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":[";"]}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":26},"action":"insert","lines":["''"],"id":22837}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":26},"action":"remove","lines":["''"],"id":22838},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":[";"]}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":25},"action":"insert","lines":["''"],"id":22839}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["A"],"id":22840},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":["D"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["B"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["E"]}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":2},"action":"insert","lines":["# "],"id":22841}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"remove","lines":["# "],"id":22842}],[{"start":{"row":66,"column":24},"end":{"row":67,"column":0},"action":"insert","lines":["",""],"id":22844},{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":67,"column":4},"end":{"row":67,"column":5},"action":"insert","lines":["l"],"id":22845},{"start":{"row":67,"column":5},"end":{"row":67,"column":6},"action":"insert","lines":["a"]},{"start":{"row":67,"column":6},"end":{"row":67,"column":7},"action":"insert","lines":["s"]},{"start":{"row":67,"column":7},"end":{"row":67,"column":8},"action":"insert","lines":["t"]},{"start":{"row":67,"column":8},"end":{"row":67,"column":9},"action":"insert","lines":["_"]},{"start":{"row":67,"column":9},"end":{"row":67,"column":10},"action":"insert","lines":["m"]},{"start":{"row":67,"column":10},"end":{"row":67,"column":11},"action":"insert","lines":["o"]},{"start":{"row":67,"column":11},"end":{"row":67,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":67,"column":12},"end":{"row":67,"column":13},"action":"insert","lines":[" "],"id":22846},{"start":{"row":67,"column":13},"end":{"row":67,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":67,"column":14},"end":{"row":67,"column":15},"action":"insert","lines":[" "],"id":22847},{"start":{"row":67,"column":15},"end":{"row":67,"column":16},"action":"insert","lines":["l"]},{"start":{"row":67,"column":16},"end":{"row":67,"column":17},"action":"insert","lines":["a"]},{"start":{"row":67,"column":17},"end":{"row":67,"column":18},"action":"insert","lines":["s"]},{"start":{"row":67,"column":18},"end":{"row":67,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":67,"column":15},"end":{"row":67,"column":19},"action":"remove","lines":["last"],"id":22848},{"start":{"row":67,"column":15},"end":{"row":67,"column":24},"action":"insert","lines":["last_date"]}],[{"start":{"row":67,"column":24},"end":{"row":67,"column":26},"action":"insert","lines":["[]"],"id":22849}],[{"start":{"row":67,"column":25},"end":{"row":67,"column":26},"action":"insert","lines":[":"],"id":22850},{"start":{"row":67,"column":26},"end":{"row":67,"column":27},"action":"insert","lines":["2"]}],[{"start":{"row":67,"column":28},"end":{"row":68,"column":0},"action":"insert","lines":["",""],"id":22851},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "]},{"start":{"row":68,"column":4},"end":{"row":68,"column":5},"action":"insert","lines":["l"]},{"start":{"row":68,"column":5},"end":{"row":68,"column":6},"action":"insert","lines":["a"]},{"start":{"row":68,"column":6},"end":{"row":68,"column":7},"action":"insert","lines":["s"]},{"start":{"row":68,"column":7},"end":{"row":68,"column":8},"action":"insert","lines":["t"]},{"start":{"row":68,"column":8},"end":{"row":68,"column":9},"action":"insert","lines":["_"]},{"start":{"row":68,"column":9},"end":{"row":68,"column":10},"action":"insert","lines":["d"]}],[{"start":{"row":68,"column":10},"end":{"row":68,"column":11},"action":"insert","lines":["a"],"id":22852},{"start":{"row":68,"column":11},"end":{"row":68,"column":12},"action":"insert","lines":["y"]}],[{"start":{"row":68,"column":12},"end":{"row":68,"column":13},"action":"insert","lines":[" "],"id":22853},{"start":{"row":68,"column":13},"end":{"row":68,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":68,"column":14},"end":{"row":68,"column":15},"action":"insert","lines":[" "],"id":22854}],[{"start":{"row":68,"column":15},"end":{"row":68,"column":16},"action":"insert","lines":["l"],"id":22855},{"start":{"row":68,"column":16},"end":{"row":68,"column":17},"action":"insert","lines":["a"]},{"start":{"row":68,"column":17},"end":{"row":68,"column":18},"action":"insert","lines":["s"]},{"start":{"row":68,"column":18},"end":{"row":68,"column":19},"action":"insert","lines":["t"]},{"start":{"row":68,"column":19},"end":{"row":68,"column":20},"action":"insert","lines":["_"]},{"start":{"row":68,"column":20},"end":{"row":68,"column":21},"action":"insert","lines":["d"]},{"start":{"row":68,"column":21},"end":{"row":68,"column":22},"action":"insert","lines":["a"]},{"start":{"row":68,"column":22},"end":{"row":68,"column":23},"action":"insert","lines":["t"]},{"start":{"row":68,"column":23},"end":{"row":68,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":68,"column":24},"end":{"row":68,"column":26},"action":"insert","lines":["[]"],"id":22856}],[{"start":{"row":68,"column":26},"end":{"row":68,"column":27},"action":"insert","lines":[" "],"id":22857},{"start":{"row":68,"column":27},"end":{"row":68,"column":28},"action":"insert","lines":["z"]},{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"insert","lines":["\""]}],[{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"remove","lines":["\""],"id":22858},{"start":{"row":68,"column":27},"end":{"row":68,"column":28},"action":"remove","lines":["z"]}],[{"start":{"row":68,"column":27},"end":{"row":68,"column":28},"action":"insert","lines":[":"],"id":22859},{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"insert","lines":["0"]}],[{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"remove","lines":["0"],"id":22860},{"start":{"row":68,"column":27},"end":{"row":68,"column":28},"action":"remove","lines":[":"]}],[{"start":{"row":68,"column":27},"end":{"row":68,"column":29},"action":"insert","lines":["\"\""],"id":22861}],[{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"insert","lines":["0"],"id":22862},{"start":{"row":68,"column":29},"end":{"row":68,"column":30},"action":"insert","lines":["1"]},{"start":{"row":68,"column":30},"end":{"row":68,"column":31},"action":"insert","lines":["/"]},{"start":{"row":68,"column":31},"end":{"row":68,"column":32},"action":"insert","lines":["0"]},{"start":{"row":68,"column":32},"end":{"row":68,"column":33},"action":"insert","lines":["1"]},{"start":{"row":68,"column":33},"end":{"row":68,"column":34},"action":"insert","lines":["/"]},{"start":{"row":68,"column":34},"end":{"row":68,"column":35},"action":"insert","lines":["2"]},{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"insert","lines":["0"]},{"start":{"row":68,"column":36},"end":{"row":68,"column":37},"action":"insert","lines":["2"]}],[{"start":{"row":68,"column":37},"end":{"row":68,"column":38},"action":"insert","lines":["0"],"id":22863}],[{"start":{"row":68,"column":25},"end":{"row":68,"column":26},"action":"insert","lines":["3"],"id":22864}],[{"start":{"row":68,"column":26},"end":{"row":68,"column":27},"action":"insert","lines":[":"],"id":22865},{"start":{"row":68,"column":27},"end":{"row":68,"column":28},"action":"insert","lines":["5"]}],[{"start":{"row":68,"column":29},"end":{"row":68,"column":30},"action":"remove","lines":[" "],"id":22866},{"start":{"row":68,"column":29},"end":{"row":69,"column":0},"action":"insert","lines":["",""]},{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"insert","lines":["    "]},{"start":{"row":69,"column":4},"end":{"row":69,"column":5},"action":"insert","lines":["l"]},{"start":{"row":69,"column":5},"end":{"row":69,"column":6},"action":"insert","lines":["s"]},{"start":{"row":69,"column":6},"end":{"row":69,"column":7},"action":"insert","lines":["a"]},{"start":{"row":69,"column":7},"end":{"row":69,"column":8},"action":"insert","lines":["t"]},{"start":{"row":69,"column":8},"end":{"row":69,"column":9},"action":"insert","lines":["="]},{"start":{"row":69,"column":8},"end":{"row":69,"column":9},"action":"remove","lines":["="]},{"start":{"row":69,"column":7},"end":{"row":69,"column":8},"action":"remove","lines":["t"]},{"start":{"row":69,"column":6},"end":{"row":69,"column":7},"action":"remove","lines":["a"]},{"start":{"row":69,"column":5},"end":{"row":69,"column":6},"action":"remove","lines":["s"]}],[{"start":{"row":69,"column":5},"end":{"row":69,"column":6},"action":"insert","lines":["a"],"id":22867},{"start":{"row":69,"column":6},"end":{"row":69,"column":7},"action":"insert","lines":["s"]},{"start":{"row":69,"column":7},"end":{"row":69,"column":8},"action":"insert","lines":["t"]},{"start":{"row":69,"column":8},"end":{"row":69,"column":9},"action":"insert","lines":["_"]},{"start":{"row":69,"column":9},"end":{"row":69,"column":10},"action":"insert","lines":["y"]},{"start":{"row":69,"column":10},"end":{"row":69,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":69,"column":10},"end":{"row":69,"column":11},"action":"remove","lines":["e"],"id":22868}],[{"start":{"row":69,"column":10},"end":{"row":69,"column":11},"action":"insert","lines":["r"],"id":22869}],[{"start":{"row":69,"column":11},"end":{"row":69,"column":12},"action":"insert","lines":[" "],"id":22870},{"start":{"row":69,"column":12},"end":{"row":69,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":69,"column":13},"end":{"row":69,"column":14},"action":"insert","lines":[" "],"id":22871}],[{"start":{"row":66,"column":24},"end":{"row":69,"column":26},"action":"remove","lines":["","    last_mon = last_date[:2]","    last_day = last_date[3:5]","    last_yr = \"01/01/2020\""],"id":22872}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"insert","lines":["# "],"id":22873}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":2},"action":"remove","lines":["# "],"id":22874}],[{"start":{"row":93,"column":4},"end":{"row":94,"column":15},"action":"remove","lines":["","# create_data()"],"id":22875}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"remove","lines":["    "],"id":22876},{"start":{"row":92,"column":4},"end":{"row":93,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":8},"action":"remove","lines":["    "],"id":22877},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":8},"end":{"row":18,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"remove","lines":["    "],"id":22878},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "]},{"start":{"row":10,"column":44},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":18},"end":{"row":4,"column":19},"action":"remove","lines":["","    ticker = 'AAPL'"],"id":22879}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":41,"column":4},"end":{"row":41,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"start","mode":"ace/mode/python"}},"timestamp":1638378090768}