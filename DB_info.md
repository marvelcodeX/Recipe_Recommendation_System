mysql\> USE recipe;  
Reading table information for completion of table and column names  
You can turn off this feature to get a quicker startup with \-A  
Database changed  
mysql\> SHOW TABLES;  
\+--------------------+  
| Tables\_in\_recipe   |  
\+--------------------+  
| favorites          |  
| ingredients        |  
| recipe\_ingredients |  
| recipes            |  
| search\_logs        |  
| submitted\_recipes  |  
| users              |  
\+--------------------+  
7 rows in set (0.002 sec)  
mysql\> SELECT \* FROM favorites;  
\+----+---------+-----------+---------------------+  
| id | user\_id | recipe\_id | favorited\_at        |  
\+----+---------+-----------+---------------------+  
|  1 |       1 |        65 | 2025-05-27 07:24:53 |  
|  2 |       3 |        68 | 2025-05-27 07:24:53 |  
|  3 |       9 |        22 | 2025-05-27 07:24:53 |  
|  4 |      10 |         6 | 2025-05-27 07:24:53 |  
|  5 |       3 |        10 | 2025-05-27 07:25:08 |  
\+----+---------+-----------+---------------------+  
5 rows in set (0.003 sec)  
mysql\> SELECT \* FROM ingredients;  
\+-----+------------------------+-----------+  
| id  | name                   | category  |  
\+-----+------------------------+-----------+  
|   1 | Onion                  | vegetable |  
|   2 | Tomato                 | vegetable |  
|   3 | Potato                 | vegetable |  
|   4 | Cauliflower            | vegetable |  
|   5 | Green Peas             | vegetable |  
|   6 | Carrot                 | vegetable |  
|   7 | Brinjal                | vegetable |  
|   8 | Okra                   | vegetable |  
|   9 | Spinach                | vegetable |  
|  10 | Fenugreek Leaves       | vegetable |  
|  11 | Bitter Gourd           | vegetable |  
|  12 | Bottle Gourd           | vegetable |  
|  13 | Pumpkin                | vegetable |  
|  14 | Drumstick              | vegetable |  
|  15 | Cabbage                | vegetable |  
|  16 | Beans                  | vegetable |  
|  17 | Green Chili            | vegetable |  
|  18 | Ginger                 | vegetable |  
|  19 | Garlic                 | vegetable |  
|  20 | Coriander Leaves       | vegetable |  
|  21 | Curry Leaves           | vegetable |  
|  22 | Mint Leaves            | vegetable |  
|  23 | Ghee                   | dairy     |  
|  24 | Butter                 | dairy     |  
|  25 | Paneer                 | dairy     |  
|  26 | Yogurt                 | dairy     |  
|  27 | Milk                   | dairy     |  
|  28 | Fresh Cream            | dairy     |  
|  29 | Chicken                | protein   |  
|  30 | Mutton                 | protein   |  
|  31 | Fish                   | protein   |  
|  32 | Prawns                 | protein   |  
|  33 | Egg                    | protein   |  
|  34 | Chana Dal              | protein   |  
|  35 | Toor Dal               | protein   |  
|  36 | Moong Dal              | protein   |  
|  37 | Urad Dal               | protein   |  
|  38 | Rajma                  | protein   |  
|  39 | Chickpeas              | protein   |  
|  40 | Soya Chunks            | protein   |  
|  41 | Turmeric Powder        | spice     |  
|  42 | Red Chili Powder       | spice     |  
|  43 | Coriander Powder       | spice     |  
|  44 | Cumin Powder           | spice     |  
|  45 | Garam Masala           | spice     |  
|  46 | Mustard Seeds          | spice     |  
|  47 | Cumin Seeds            | spice     |  
|  48 | Fennel Seeds           | spice     |  
|  49 | Fenugreek Seeds        | spice     |  
|  50 | Asafoetida             | spice     |  
|  51 | Cardamom               | spice     |  
|  52 | Cloves                 | spice     |  
|  53 | Cinnamon               | spice     |  
|  54 | Bay Leaf               | spice     |  
|  55 | Black Pepper           | spice     |  
|  56 | Carom Seeds            | spice     |  
|  57 | Dried Fenugreek Leaves | spice     |  
|  58 | Star Anise             | spice     |  
|  59 | Basmati Rice           | grain     |  
|  60 | Rice                   | grain     |  
|  61 | Wheat Flour            | grain     |  
|  62 | Semolina               | grain     |  
|  63 | Gram Flour             | grain     |  
|  64 | Rice Flour             | grain     |  
|  65 | Poha                   | grain     |  
|  66 | Sabudana               | grain     |  
|  67 | Oil                    | other     |  
|  68 | Salt                   | other     |  
|  69 | Sugar                  | other     |  
|  70 | Jaggery                | other     |  
|  71 | Tamarind               | other     |  
|  72 | Coconut                | other     |  
|  73 | Coconut Milk           | other     |  
|  74 | Lemon                  | other     |  
|  75 | Vinegar                | other     |  
|  76 | Sago                   | grain     |  
|  77 | Jackfruit              | vegetable |  
|  78 | Fox Nuts               | other     |  
|  79 | Ridge Gourd            | vegetable |  
|  80 | Snake Gourd            | vegetable |  
|  81 | Banana Flower          | vegetable |  
|  82 | Arrowroot              | grain     |  
|  83 | Black Chickpeas        | protein   |  
|  84 | Horse Gram             | protein   |  
|  85 | Taro Root              | vegetable |  
|  86 | Banana Stem            | vegetable |  
|  87 | Cluster Beans          | vegetable |  
|  88 | Raw Mango              | vegetable |  
|  89 | Sorrel Leaves          | vegetable |  
|  90 | Colocasia Leaves       | vegetable |  
|  91 | Yogurt Marinated       | dairy     |  
|  92 | Pomegranate Seeds      | vegetable |  
|  93 | Rose Water             | other     |  
|  94 | Saffron                | spice     |  
|  95 | Edible Gum             | other     |  
|  96 | Tofu                   | protein   |  
|  97 | Soy Sauce              | other     |  
|  98 | Sesame Oil             | other     |  
|  99 | Rice Vinegar           | other     |  
| 100 | Szechuan Pepper        | spice     |  
\+-----+------------------------+-----------+  
100 rows in set (0.003 sec)  
mysql\> SELECT \* FROM recipe\_ingredients;  
\+-----------+---------------+-------------+  
| recipe\_id | ingredient\_id | quantity    |  
\+-----------+---------------+-------------+  
|         1 |             1 | 2 medium    |  
|         1 |             2 | 4 medium    |  
|         1 |            18 | 1 inch      |  
|         1 |            19 | 6 cloves    |  
|         1 |            23 | 2 tbsp      |  
|         1 |            26 | 1/2 cup     |  
|         1 |            28 | 1/4 cup     |  
|         1 |            29 | 500g        |  
|         1 |            41 | 1/2 tsp     |  
|         1 |            42 | 1 tsp       |  
|         1 |            45 | 1 tsp       |  
|         2 |             9 | 2 bunches   |  
|         2 |            17 | 2           |  
|         2 |            18 | 1 inch      |  
|         2 |            19 | 4 cloves    |  
|         2 |            23 | 2 tbsp      |  
|         2 |            25 | 200g        |  
|         2 |            28 | 2 tbsp      |  
|         2 |            41 | 1/2 tsp     |  
|         2 |            47 | 1/2 tsp     |  
|         3 |             1 | 1 large     |  
|         3 |            26 | 1/4 cup     |  
|         3 |            39 | 1 cup       |  
|         3 |            41 | 1/2 tsp     |  
|         3 |            42 | 1 tsp       |  
|         3 |            43 | 1 tsp       |  
|         3 |            45 | 1/2 tsp     |  
|         3 |            61 | 2 cups      |  
|         3 |            67 | for frying  |  
|         4 |             1 | 2 medium    |  
|         4 |             2 | 3 medium    |  
|         4 |            18 | 1 inch      |  
|         4 |            19 | 4 cloves    |  
|         4 |            38 | 1 cup       |  
|         4 |            41 | 1/2 tsp     |  
|         4 |            42 | 1 tsp       |  
|         4 |            45 | 1 tsp       |  
|         4 |            59 | 1 cup       |  
|         5 |             3 | 3 medium    |  
|         5 |            17 | 2           |  
|         5 |            20 | for garnish |  
|         5 |            23 | 2 tbsp      |  
|         5 |            41 | 1/4 tsp     |  
|         5 |            47 | 1/2 tsp     |  
|         5 |            61 | 2 cups      |  
|         5 |            68 | to taste    |  
|         6 |             1 | 1 large     |  
|         6 |             2 | 2 medium    |  
|         6 |            18 | 1 inch      |  
|         6 |            19 | 6 cloves    |  
|         6 |            23 | 2 tbsp      |  
|         6 |            28 | 1/4 cup     |  
|         6 |            37 | 1/2 cup     |  
|         6 |            38 | 1/4 cup     |  
|         6 |            45 | 1 tsp       |  
|         7 |             1 | 1 large     |  
|         7 |             2 | 3 medium    |  
|         7 |            17 | 2-3         |  
|         7 |            23 | 2 tbsp      |  
|         7 |            25 | 250g        |  
|         7 |            28 | 2 tbsp      |  
|         7 |            42 | 1 tsp       |  
|         7 |            43 | 1 tsp       |  
|         7 |            45 | 1 tsp       |  
|         8 |             1 | 2 large     |  
|         8 |             2 | 3 medium    |  
|         8 |            18 | 1 inch      |  
|         8 |            19 | 8 cloves    |  
|         8 |            23 | 3 tbsp      |  
|         8 |            26 | 1/2 cup     |  
|         8 |            30 | 500g        |  
|         8 |            42 | 1 tsp       |  
|         8 |            45 | 1.5 tsp     |  
|         9 |             1 | 1 large     |  
|         9 |             2 | 3 medium    |  
|         9 |             3 | 2 medium    |  
|         9 |            23 | 3 tbsp      |  
|         9 |            25 | 100g        |  
|         9 |            28 | 1/2 cup     |  
|         9 |            45 | 1 tsp       |  
|         9 |            61 | 2 tbsp      |  
|         9 |            63 | 2 tbsp      |  
|        10 |            18 | 2 inch      |  
|        10 |            19 | 10 cloves   |  
|        10 |            23 | 2 tbsp      |  
|        10 |            26 | 1 cup       |  
|        10 |            29 | 1kg         |  
|        10 |            41 | 1 tsp       |  
|        10 |            42 | 1 tbsp      |  
|        10 |            45 | 1 tbsp      |  
|        10 |            74 | 2 tbsp      |  
|        11 |             1 | 1 large     |  
|        11 |             3 | 3 medium    |  
|        11 |            17 | 2-3         |  
|        11 |            37 | 1/2 cup     |  
|        11 |            41 | 1/4 tsp     |  
|        11 |            47 | 1/2 tsp     |  
|        11 |            59 | 2 cups      |  
|        11 |            67 | for cooking |  
|        11 |            68 | to taste    |  
|        12 |             1 | 1 large     |  
|        12 |             2 | 2 medium    |  
|        12 |            35 | 1/2 cup     |  
|        12 |            37 | 1 cup       |  
|        12 |            41 | 1/2 tsp     |  
|        12 |            42 | 1 tsp       |  
|        12 |            47 | 1/2 tsp     |  
|        12 |            59 | 2 cups      |  
|        12 |            71 | small ball  |  
|        13 |             1 | 1 small     |  
|        13 |            17 | 2-3         |  
|        13 |            21 | few sprigs  |  
|        13 |            37 | 1 cup       |  
|        13 |            41 | 1/4 tsp     |  
|        13 |            47 | 1/2 tsp     |  
|        13 |            67 | for frying  |  
|        13 |            68 | to taste    |  
|        14 |             1 | 1 large     |  
|        14 |             2 | 2 medium    |  
|        14 |            23 | 2 tbsp      |  
|        14 |            35 | 1/2 cup     |  
|        14 |            42 | 1 tsp       |  
|        14 |            45 | 1 tbsp      |  
|        14 |            59 | 1 cup       |  
|        14 |            71 | small ball  |  
|        14 |            72 | 1/4 cup     |  
|        15 |            21 | few sprigs  |  
|        15 |            23 | 2 tbsp      |  
|        15 |            36 | 1/4 cup     |  
|        15 |            47 | 1 tsp       |  
|        15 |            56 | 1/2 tsp     |  
|        15 |            59 | 1 cup       |  
|        15 |            67 | 1 tbsp      |  
|        15 |            68 | to taste    |  
|        16 |             3 | 1 medium    |  
|        16 |             6 | 1 medium    |  
|        16 |             8 | 10-12       |  
|        16 |            13 | 100g        |  
|        16 |            14 | 2           |  
|        16 |            17 | 2-3         |  
|        16 |            23 | 2 tbsp      |  
|        16 |            68 | to taste    |  
|        16 |            72 | 1/2 cup     |  
|        17 |             1 | 1 large     |  
|        17 |             2 | 1 medium    |  
|        17 |            23 | 2 tbsp      |  
|        17 |            31 | 500g        |  
|        17 |            41 | 1/2 tsp     |  
|        17 |            42 | 1 tsp       |  
|        17 |            46 | 1 tsp       |  
|        17 |            71 | small ball  |  
|        17 |            72 | 1/2 cup     |  
|        18 |            23 | 2 tbsp      |  
|        18 |            41 | 1/2 tsp     |  
|        18 |            42 | 1 tsp       |  
|        18 |            46 | 1/2 tsp     |  
|        18 |            47 | 1 tsp       |  
|        18 |            59 | 2 cups      |  
|        18 |            68 | to taste    |  
|        18 |            71 | lemon sized |  
|        18 |            72 | 1/4 cup     |  
|        19 |            26 | 1/2 cup     |  
|        19 |            27 | 1/2 cup     |  
|        19 |            59 | 2 cups      |  
|        19 |            67 | for cooking |  
|        19 |            68 | to taste    |  
|        19 |            69 | 1 tsp       |  
|        20 |             5 | 1 cup       |  
|        20 |            21 | few sprigs  |  
|        20 |            23 | 1 tbsp      |  
|        20 |            41 | 1/4 tsp     |  
|        20 |            46 | 1/2 tsp     |  
|        20 |            47 | 1/2 tsp     |  
|        20 |            68 | to taste    |  
|        20 |            72 | 2 tbsp      |  
|        21 |             1 | 2 medium    |  
|        21 |             2 | 1 medium    |  
|        21 |            17 | 2-3         |  
|        21 |            23 | 2 tbsp      |  
|        21 |            31 | 500g        |  
|        21 |            41 | 1/2 tsp     |  
|        21 |            42 | 1 tsp       |  
|        21 |            47 | 1/2 tsp     |  
|        21 |            68 | to taste    |  
|        22 |            27 | 1 liter     |  
|        22 |            68 | pinch       |  
|        22 |            69 | 1.5 cups    |  
|        22 |            72 | for garnish |  
|        22 |            74 | 1 tbsp      |  
|        23 |            26 | 2 tbsp      |  
|        23 |            27 | 1 liter     |  
|        23 |            70 | 1/2 cup     |  
|        24 |             1 | 1 large     |  
|        24 |             2 | 2 medium    |  
|        24 |             3 | 3 medium    |  
|        24 |            17 | 2-3         |  
|        24 |            23 | 2 tbsp      |  
|        24 |            61 | 2 cups      |  
|        24 |            63 | 1/2 cup     |  
|        24 |            68 | to taste    |  
|        25 |             3 | 3 medium    |  
|        25 |            17 | 2-3         |  
|        25 |            23 | 2 tbsp      |  
|        25 |            41 | 1/4 tsp     |  
|        25 |            47 | 1/2 tsp     |  
|        25 |            49 | 2 tbsp      |  
|        25 |            68 | to taste    |  
|        26 |            17 | 2           |  
|        26 |            18 | 1 inch      |  
|        26 |            23 | 2 tbsp      |  
|        26 |            32 | 250g        |  
|        26 |            41 | 1/4 tsp     |  
|        26 |            45 | 1/2 tsp     |  
|        26 |            68 | to taste    |  
|        26 |            73 | 1 cup       |  
|        27 |            23 | 1 tbsp      |  
|        27 |            27 | 1/2 cup     |  
|        27 |            59 | 2 cups      |  
|        27 |            69 | 1/4 cup     |  
|        27 |            70 | 1/2 cup     |  
|        27 |            72 | 1/4 cup     |  
|        28 |             3 | 1 medium    |  
|        28 |             5 | 1/2 cup     |  
|        28 |             6 | 1 medium    |  
|        28 |            23 | 2 tbsp      |  
|        28 |            35 | 1 cup       |  
|        28 |            41 | 1/2 tsp     |  
|        28 |            47 | 1 tsp       |  
|        28 |            68 | to taste    |  
|        29 |            17 | 3-4         |  
|        29 |            23 | 2 tbsp      |  
|        29 |            31 | 500g        |  
|        29 |            41 | 1/2 tsp     |  
|        29 |            46 | 2 tbsp      |  
|        29 |            68 | to taste    |  
|        29 |            74 | 1 tbsp      |  
|        30 |            25 | 200g        |  
|        30 |            27 | 1/4 cup     |  
|        30 |            51 | 2 pods      |  
|        30 |            69 | 1/2 cup     |  
|        30 |            72 | 2 tbsp      |  
|        31 |             1 | 2 large     |  
|        31 |             2 | 3 medium    |  
|        31 |             3 | 3 medium    |  
|        31 |             4 | 1/2 small   |  
|        31 |             6 | 2 medium    |  
|        31 |            23 | 3 tbsp      |  
|        31 |            42 | 1 tsp       |  
|        31 |            45 | 1 tbsp      |  
|        31 |            68 | to taste    |  
|        32 |             3 | 4 medium    |  
|        32 |            17 | 2-3         |  
|        32 |            41 | 1/2 tsp     |  
|        32 |            47 | 1 tsp       |  
|        32 |            61 | 1/2 cup     |  
|        32 |            67 | for frying  |  
|        32 |            68 | to taste    |  
|        33 |            26 | 1/2 cup     |  
|        33 |            47 | 1/2 tsp     |  
|        33 |            63 | 1 cup       |  
|        33 |            67 | 1 tsp       |  
|        33 |            68 | to taste    |  
|        33 |            74 | 1 tbsp      |  
|        34 |            10 | 1/4 cup     |  
|        34 |            23 | 2 tbsp      |  
|        34 |            26 | 2 tbsp      |  
|        34 |            41 | 1/2 tsp     |  
|        34 |            42 | 1/2 tsp     |  
|        34 |            61 | 2 cups      |  
|        34 |            68 | to taste    |  
|        35 |             5 | 1/2 cup     |  
|        35 |             8 | 10-12       |  
|        35 |            11 | 2 medium    |  
|        35 |            12 | 1 small     |  
|        35 |            23 | 3 tbsp      |  
|        35 |            45 | 1 tbsp      |  
|        35 |            63 | 1/4 cup     |  
|        35 |            68 | to taste    |  
|        36 |            18 | 1 inch      |  
|        36 |            23 | 2 tbsp      |  
|        36 |            26 | 1/2 cup     |  
|        36 |            41 | 1/4 tsp     |  
|        36 |            47 | 1/2 tsp     |  
|        36 |            63 | 1 cup       |  
|        36 |            68 | to taste    |  
|        37 |            17 | 1-2         |  
|        37 |            68 | to taste    |  
|        37 |            72 | for garnish |  
|        37 |            73 | 1 cup       |  
|        38 |            31 | 500g        |  
|        38 |            41 | 1/2 tsp     |  
|        38 |            42 | 1 tsp       |  
|        38 |            62 | 1/2 cup     |  
|        38 |            67 | for frying  |  
|        38 |            68 | to taste    |  
|        38 |            74 | 1 tbsp      |  
|        39 |            23 | 1 tbsp      |  
|        39 |            51 | 2 pods      |  
|        39 |            59 | 1 cup       |  
|        39 |            69 | 1/4 cup     |  
|        39 |            70 | 1/2 cup     |  
|        39 |            72 | 1/2 cup     |  
|        40 |            23 | 3 tbsp      |  
|        40 |            35 | 1 cup       |  
|        40 |            51 | 2 pods      |  
|        40 |            61 | 2 cups      |  
|        40 |            68 | pinch       |  
|        40 |            70 | 1/2 cup     |  
|        41 |            17 | 2-3         |  
|        41 |            20 | 1/4 cup     |  
|        41 |            21 | 1/4 cup     |  
|        41 |            63 | 1 cup       |  
|        41 |            68 | to taste    |  
|        41 |            71 | small ball  |  
|        41 |            74 | 2 tbsp      |  
|        42 |             2 | 1 small     |  
|        42 |            20 | 1/4 cup     |  
|        42 |            21 | 1/4 cup     |  
|        42 |            65 | 2 cups      |  
|        42 |            68 | to taste    |  
|        42 |            71 | 1 tsp       |  
|        42 |            74 | 1 tbsp      |  
|        43 |             2 | 1 small     |  
|        43 |            20 | 1/4 cup     |  
|        43 |            21 | 1/4 cup     |  
|        43 |            26 | 1 cup       |  
|        43 |            63 | 1 cup       |  
|        43 |            68 | to taste    |  
|        43 |            71 | 1 tsp       |  
|        44 |             3 | 3 medium    |  
|        44 |             5 | 1/4 cup     |  
|        44 |            17 | 2-3         |  
|        44 |            41 | 1/2 tsp     |  
|        44 |            47 | 1 tsp       |  
|        44 |            61 | 2 cups      |  
|        44 |            67 | for frying  |  
|        44 |            68 | to taste    |  
|        45 |            34 | 1/2 cup     |  
|        45 |            42 | 1/2 tsp     |  
|        45 |            45 | 1/2 tsp     |  
|        45 |            47 | 1 tsp       |  
|        45 |            61 | 2 cups      |  
|        45 |            67 | for frying  |  
|        45 |            68 | to taste    |  
|        46 |            51 | 2 pods      |  
|        46 |            63 | 1 cup       |  
|        46 |            67 | for frying  |  
|        46 |            69 | 1.5 cups    |  
|        46 |            74 | 1 tbsp      |  
|        47 |             3 | 2 medium    |  
|        47 |            20 | 1/4 cup     |  
|        47 |            21 | 1/4 cup     |  
|        47 |            26 | 1/2 cup     |  
|        47 |            65 | 2 cups      |  
|        47 |            68 | to taste    |  
|        47 |            71 | 1 tsp       |  
|        48 |             3 | 4 medium    |  
|        48 |             5 | 1/4 cup     |  
|        48 |            17 | 2-3         |  
|        48 |            41 | 1/2 tsp     |  
|        48 |            47 | 1 tsp       |  
|        48 |            67 | for frying  |  
|        48 |            68 | to taste    |  
|        49 |             1 | 2 large     |  
|        49 |             2 | 3 medium    |  
|        49 |             3 | 3 medium    |  
|        49 |             4 | 1/2 small   |  
|        49 |             6 | 2 medium    |  
|        49 |            23 | 3 tbsp      |  
|        49 |            42 | 1 tsp       |  
|        49 |            45 | 1 tbsp      |  
|        49 |            68 | to taste    |  
|        50 |             1 | 1 large     |  
|        50 |             2 | 2 medium    |  
|        50 |             3 | 4 medium    |  
|        50 |            20 | 1/4 cup     |  
|        50 |            21 | 1/4 cup     |  
|        50 |            39 | 1 cup       |  
|        50 |            42 | 1 tsp       |  
|        50 |            45 | 1 tsp       |  
|        50 |            68 | to taste    |  
|        51 |             1 | 2 large     |  
|        51 |            18 | 2 inch      |  
|        51 |            23 | 3 tbsp      |  
|        51 |            26 | 1/2 cup     |  
|        51 |            30 | 500g        |  
|        51 |            41 | 1/2 tsp     |  
|        51 |            45 | 1.5 tsp     |  
|        51 |            58 | 2 pieces    |  
|        51 |            74 | 1 tbsp      |  
|        52 |             1 | 1 large     |  
|        52 |             9 | 1 bunch     |  
|        52 |            10 | 2 bunches   |  
|        52 |            17 | 3-4         |  
|        52 |            18 | 1 inch      |  
|        52 |            23 | 3 tbsp      |  
|        52 |            41 | 1/2 tsp     |  
|        52 |            42 | 1 tsp       |  
|        52 |            68 | to taste    |  
|        53 |            27 | 2 cups      |  
|        53 |            51 | 2 pods      |  
|        53 |            53 | 1/2 inch    |  
|        53 |            55 | 4-5         |  
|        53 |            68 | pinch       |  
|        53 |            70 | 2 tbsp      |  
|        54 |             1 | 1 large     |  
|        54 |             3 | 15 small    |  
|        54 |            23 | 3 tbsp      |  
|        54 |            26 | 1/2 cup     |  
|        54 |            41 | 1/4 tsp     |  
|        54 |            42 | 1/2 tsp     |  
|        54 |            45 | 1 tsp       |  
|        54 |            68 | to taste    |  
|        55 |            10 | 1/2 bunch   |  
|        55 |            17 | 1           |  
|        55 |            26 | 1 cup       |  
|        55 |            41 | 1/4 tsp     |  
|        55 |            47 | 1/2 tsp     |  
|        55 |            68 | to taste    |  
|        56 |            17 | 2-3         |  
|        56 |            18 | 1 inch      |  
|        56 |            36 | 1 cup       |  
|        56 |            47 | 1/2 tsp     |  
|        56 |            67 | for cooking |  
|        56 |            68 | to taste    |  
|        57 |            37 | 1/4 cup     |  
|        57 |            41 | 1/4 tsp     |  
|        57 |            46 | 1/2 tsp     |  
|        57 |            47 | 1 tsp       |  
|        57 |            64 | 2 cups      |  
|        57 |            67 | 2 tbsp      |  
|        57 |            68 | to taste    |  
|        58 |            23 | 1/4 cup     |  
|        58 |            26 | 1/2 cup     |  
|        58 |            29 | 500g        |  
|        58 |            45 | 1.5 tsp     |  
|        58 |            58 | 2 pieces    |  
|        58 |            59 | 2 cups      |  
|        58 |            68 | to taste    |  
|        58 |            72 | 1/2 cup     |  
|        58 |            74 | 2 tbsp      |  
|        59 |            12 | 1 small     |  
|        59 |            13 | 100g        |  
|        59 |            21 | few sprigs  |  
|        59 |            23 | 2 tbsp      |  
|        59 |            41 | 1/2 tsp     |  
|        59 |            47 | 1 tsp       |  
|        59 |            68 | to taste    |  
|        59 |            72 | 1/2 cup     |  
|        60 |            60 | 2 cups      |  
|        60 |            67 | for cooking |  
|        60 |            68 | to taste    |  
|        60 |            72 | 1/4 cup     |  
|        61 |             1 | 1 large     |  
|        61 |            21 | for garnish |  
|        61 |            23 | 2 tbsp      |  
|        61 |            31 | 1 head      |  
|        61 |            41 | 1/2 tsp     |  
|        61 |            45 | 1 tsp       |  
|        61 |            60 | 1 cup       |  
|        61 |            68 | to taste    |  
|        62 |            36 | 1/4 cup     |  
|        62 |            60 | 2 cups      |  
|        62 |            67 | for cooking |  
|        62 |            68 | pinch       |  
|        62 |            70 | 1 tbsp      |  
|        63 |            17 | 3-4         |  
|        63 |            49 | 1/2 cup     |  
|        63 |            68 | to taste    |  
|        63 |            71 | small piece |  
|        63 |            74 | 1 tbsp      |  
|        64 |             1 | 1 large     |  
|        64 |            23 | 2 tbsp      |  
|        64 |            29 | 500g        |  
|        64 |            42 | 1.5 tsp     |  
|        64 |            45 | 1 tsp       |  
|        64 |            68 | to taste    |  
|        64 |            72 | 1/2 cup     |  
|        65 |            27 | 1/2 cup     |  
|        65 |            60 | 1 cup       |  
|        65 |            67 | for cooking |  
|        65 |            69 | 1 tbsp      |  
|        65 |            70 | 1/2 cup     |  
|        65 |            72 | 1/2 cup     |  
|        66 |             3 | 1 medium    |  
|        66 |            17 | 2-3         |  
|        66 |            23 | 1 tbsp      |  
|        66 |            47 | 1 tsp       |  
|        66 |            66 | 1 cup       |  
|        66 |            68 | to taste    |  
|        66 |            74 | 1 tbsp      |  
|        67 |            17 | 8-10        |  
|        67 |            19 | 8-10        |  
|        67 |            23 | 1 tbsp      |  
|        67 |            68 | to taste    |  
|        67 |            74 | 1 tbsp      |  
|        68 |            23 | 1 tsp       |  
|        68 |            25 | 1 cup       |  
|        68 |            27 | 1/4 cup     |  
|        68 |            51 | 2 pods      |  
|        68 |            69 | 1/2 cup     |  
|        69 |            26 | 1/4 cup     |  
|        69 |            60 | 2 cups      |  
|        69 |            67 | for cooking |  
|        69 |            68 | to taste    |  
|        69 |            72 | 2 tbsp      |  
|        70 |            23 | 1 tsp       |  
|        70 |            27 | 1 liter     |  
|        70 |            51 | 4 pods      |  
|        70 |            69 | 1/2 cup     |  
|        70 |            72 | 2 tbsp      |  
|        71 |             2 | 3 medium    |  
|        71 |            18 | 1 inch      |  
|        71 |            19 | 4 cloves    |  
|        71 |            20 | for garnish |  
|        71 |            26 | 1/2 cup     |  
|        71 |            28 | 1/4 cup     |  
|        71 |            41 | 1/2 tsp     |  
|        71 |            45 | 1 tsp       |  
|        71 |            96 | 400g        |  
|        73 |             1 | 1 large     |  
|        73 |             2 | 2 medium    |  
|        73 |            17 | 2           |  
|        73 |            20 | 2 tbsp      |  
|        73 |            41 | 1/2 tsp     |  
|        73 |            43 | 1 tsp       |  
|        73 |            47 | 1 tsp       |  
|        73 |            96 | 350g        |  
\+-----------+---------------+-------------+  
528 rows in set (0.004 sec)  
mysql\> SELECT \* FROM recipes;  
\+----+---------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------+---------------------+--------+  
| id | title               | description                                            | steps                                                                                                                       | created\_by | created\_at          | rating |  
\+----+---------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------+---------------------+--------+  
|  1 | Butter Chicken      | Creamy tomato-based curry with tender chicken pieces   | 1\. Marinate chicken  
2\. Prepare gravy  
3\. Cook together                                                                       |          1 | 2025-05-27 06:46:23 |    4.8 |  
|  2 | Palak Paneer        | Spinach curry with soft cottage cheese cubes           | 1\. Blanch spinach  
2\. Make puree  
3\. Cook with spices and paneer                                                              |          1 | 2025-05-27 06:46:23 |    4.7 |  
|  3 | Chole Bhature       | Spicy chickpeas with fried bread                       | 1\. Soak chickpeas  
2\. Pressure cook  
3\. Prepare bhature dough  
4\. Fry                                                          |          1 | 2025-05-27 06:46:23 |    4.6 |  
|  4 | Rajma Chawal        | Kidney beans curry with rice                           | 1\. Soak rajma  
2\. Cook with spices  
3\. Serve with rice                                                                        |          1 | 2025-05-27 06:46:23 |    4.5 |  
|  5 | Aloo Paratha        | Stuffed potato flatbread                               | 1\. Prepare dough  
2\. Make potato stuffing  
3\. Stuff and cook                                                                  |          1 | 2025-05-27 06:46:23 |    4.4 |  
|  6 | Dal Makhani         | Creamy black lentils                                   | 1\. Soak lentils  
2\. Slow cook  
3\. Add cream                                                                                   |          1 | 2025-05-27 06:46:23 |    4.9 |  
|  7 | Kadai Paneer        | Paneer in spicy gravy with capsicum                    | 1\. Saute paneer  
2\. Prepare kadai masala  
3\. Combine                                                                          |          1 | 2025-05-27 06:46:23 |    4.6 |  
|  8 | Rogan Josh          | Aromatic lamb curry                                    | 1\. Marinate meat  
2\. Prepare gravy  
3\. Slow cook                                                                              |          1 | 2025-05-27 06:46:23 |    4.7 |  
|  9 | Malai Kofta         | Vegetable balls in creamy sauce                        | 1\. Make koftas  
2\. Prepare gravy  
3\. Combine                                                                                  |          1 | 2025-05-27 06:46:23 |    4.5 |  
| 10 | Tandoori Chicken    | Marinated grilled chicken                              | 1\. Prepare marinade  
2\. Marinate chicken  
3\. Grill                                                                            |          1 | 2025-05-27 06:46:23 |    4.8 |  
| 11 | Masala Dosa         | Crispy rice crepe with potato filling                  | 1\. Prepare batter  
2\. Ferment  
3\. Make potato bhaji  
4\. Serve                                                                  |          1 | 2025-05-27 06:46:23 |    4.7 |  
| 12 | Idli Sambar         | Steamed rice cakes with lentil stew                    | 1\. Prepare batter  
2\. Steam idlis  
3\. Cook sambar                                                                             |          1 | 2025-05-27 06:46:23 |    4.6 |  
| 13 | Vada                | Savory fried lentil donuts                             | 1\. Soak lentils  
2\. Grind  
3\. Shape and fry                                                                                   |          1 | 2025-05-27 06:46:23 |    4.5 |  
| 14 | Bisi Bele Bath      | Spicy rice-lentil dish                                 | 1\. Cook rice and dal  
2\. Prepare masala  
3\. Combine                                                                           |          1 | 2025-05-27 06:46:23 |    4.4 |  
| 15 | Pongal              | Rice-lentil porridge                                   | 1\. Pressure cook rice-dal  
2\. Temper spices                                                                                  |          1 | 2025-05-27 06:46:23 |    4.3 |  
| 16 | Avial               | Mixed vegetable curry                                  | 1\. Cut vegetables  
2\. Cook with coconut paste                                                                                |          1 | 2025-05-27 06:46:23 |    4.2 |  
| 17 | Meen Curry          | Spicy fish curry                                       | 1\. Marinate fish  
2\. Prepare gravy  
3\. Cook fish                                                                              |          1 | 2025-05-27 06:46:23 |    4.6 |  
| 18 | Puliyodarai         | Tamarind rice                                          | 1\. Prepare tamarind paste  
2\. Mix with rice                                                                                  |          1 | 2025-05-27 06:46:23 |    4.3 |  
| 19 | Appam               | Lacy rice pancakes                                     | 1\. Prepare batter  
2\. Ferment  
3\. Cook in appam pan                                                                           |          1 | 2025-05-27 06:46:23 |    4.4 |  
| 20 | Poriyal             | Stir-fried vegetables                                  | 1\. Chop vegetables  
2\. Temper spices  
3\. Stir-fry                                                                             |          1 | 2025-05-27 06:46:23 |    4.1 |  
| 21 | Macher Jhol         | Bengali fish curry                                     | 1\. Fry fish  
2\. Prepare light gravy  
3\. Combine                                                                               |          1 | 2025-05-27 06:46:23 |    4.5 |  
| 22 | Rasgulla            | Syrup-soaked cheese balls                              | 1\. Prepare chenna  
2\. Shape balls  
3\. Cook in syrup                                                                           |          1 | 2025-05-27 06:46:23 |    4.8 |  
| 23 | Mishti Doi          | Sweetened yogurt                                       | 1\. Boil milk  
2\. Add jaggery  
3\. Set curd                                                                                     |          1 | 2025-05-27 06:46:23 |    4.6 |  
| 24 | Litti Chokha        | Baked dough balls with mashed vegetables               | 1\. Prepare dough  
2\. Make stuffing  
3\. Bake  
4\. Prepare chokha                                                                 |          1 | 2025-05-27 06:46:23 |    4.3 |  
| 25 | Aloo Posto          | Potatoes in poppy seed paste                           | 1\. Fry potatoes  
2\. Prepare posto paste  
3\. Combine                                                                           |          1 | 2025-05-27 06:46:23 |    4.2 |  
| 26 | Chingri Malai Curry | Prawns in coconut milk                                 | 1\. Marinate prawns  
2\. Prepare coconut gravy  
3\. Cook prawns                                                                  |          1 | 2025-05-27 06:46:23 |    4.7 |  
| 27 | Pitha               | Rice cakes                                             | 1\. Prepare rice flour  
2\. Shape  
3\. Steam/fry                                                                                 |          1 | 2025-05-27 06:46:23 |    4.1 |  
| 28 | Dalma               | Odisha style dal with vegetables                       | 1\. Cook dal  
2\. Add vegetables  
3\. Temper                                                                                     |          1 | 2025-05-27 06:46:23 |      4 |  
| 29 | Shorshe Ilish       | Hilsa fish in mustard sauce                            | 1\. Marinate fish  
2\. Prepare mustard paste  
3\. Steam cook                                                                     |          1 | 2025-05-27 06:46:23 |    4.8 |  
| 30 | Chhena Poda         | Caramelized cheese dessert                             | 1\. Prepare chenna  
2\. Bake with sugar                                                                                        |          1 | 2025-05-27 06:46:23 |    4.7 |  
| 31 | Pav Bhaji           | Spiced vegetable mash with bread                       | 1\. Boil vegetables  
2\. Mash with spices  
3\. Serve with pav                                                                    |          1 | 2025-05-27 06:46:23 |    4.8 |  
| 32 | Vada Pav            | Potato fritter sandwich                                | 1\. Make batata vada  
2\. Place in bun  
3\. Add chutneys                                                                         |          1 | 2025-05-27 06:46:23 |    4.7 |  
| 33 | Dhokla              | Steamed fermented snack                                | 1\. Prepare batter  
2\. Ferment  
3\. Steam                                                                                       |          1 | 2025-05-27 06:46:23 |    4.6 |  
| 34 | Thepla              | Spiced fenugreek flatbread                             | 1\. Prepare dough  
2\. Roll and cook                                                                                           |          1 | 2025-05-27 06:46:23 |    4.3 |  
| 35 | Undhiyu             | Mixed winter vegetable dish                            | 1\. Prepare vegetables  
2\. Layer in pot  
3\. Slow cook                                                                          |          1 | 2025-05-27 06:46:23 |    4.4 |  
| 36 | Khandvi             | Chickpea flour rolls                                   | 1\. Prepare batter  
2\. Spread thin  
3\. Roll                                                                                    |          1 | 2025-05-27 06:46:23 |    4.2 |  
| 37 | Solkadhi            | Kokum-coconut drink                                    | 1\. Extract coconut milk  
2\. Mix with kokum                                                                                   |          1 | 2025-05-27 06:46:23 |    4.1 |  
| 38 | Bombay Duck Fry     | Crispy fried fish                                      | 1\. Marinate fish  
2\. Coat with semolina  
3\. Fry                                                                               |          1 | 2025-05-27 06:46:23 |    4.5 |  
| 39 | Modak               | Sweet rice dumplings                                   | 1\. Prepare outer covering  
2\. Make stuffing  
3\. Shape and steam                                                               |          1 | 2025-05-27 06:46:23 |    4.7 |  
| 40 | Puran Poli          | Sweet stuffed flatbread                                | 1\. Prepare lentil-jaggery filling  
2\. Make dough  
3\. Stuff and cook                                                           |          1 | 2025-05-27 06:46:23 |    4.6 |  
| 41 | Pani Puri           | Crisp puris with flavored water                        | 1\. Make puris  
2\. Prepare fillings  
3\. Assemble                                                                               |          1 | 2025-05-27 06:46:23 |    4.9 |  
| 42 | Bhel Puri           | Puffed rice snack                                      | 1\. Mix ingredients  
2\. Add chutneys  
3\. Serve immediately                                                                     |          1 | 2025-05-27 06:46:23 |    4.7 |  
| 43 | Dahi Puri           | Yogurt-filled puris                                    | 1\. Prepare puris  
2\. Fill with yogurt mixture                                                                                |          1 | 2025-05-27 06:46:23 |    4.8 |  
| 44 | Samosa              | Spiced potato pastry                                   | 1\. Prepare dough  
2\. Make filling  
3\. Shape and fry                                                                           |          1 | 2025-05-27 06:46:23 |    4.7 |  
| 45 | Kachori             | Fried stuffed pastry                                   | 1\. Make dough  
2\. Prepare filling  
3\. Stuff and fry                                                                           |          1 | 2025-05-27 06:46:23 |    4.6 |  
| 46 | Jalebi              | Crispy sweet swirls                                    | 1\. Prepare batter  
2\. Pipe in hot oil  
3\. Soak in syrup                                                                       |          1 | 2025-05-27 06:46:23 |    4.8 |  
| 47 | Chaat               | Savory snack mix                                       | 1\. Prepare base  
2\. Add toppings  
3\. Add chutneys                                                                             |          1 | 2025-05-27 06:46:23 |    4.5 |  
| 48 | Aloo Tikki          | Spiced potato patties                                  | 1\. Mash potatoes  
2\. Shape and fry  
3\. Serve with chutney                                                                     |          1 | 2025-05-27 06:46:23 |    4.4 |  
| 49 | Pav Bhaji           | Spiced vegetable mash with bread                       | 1\. Boil vegetables  
2\. Mash with spices  
3\. Serve with pav                                                                    |          1 | 2025-05-27 06:46:23 |    4.8 |  
| 50 | Ragda Pattice       | Potato patties with pea curry                          | 1\. Make patties  
2\. Prepare ragda  
3\. Combine                                                                                 |          1 | 2025-05-27 06:46:23 |    4.6 |  
| 51 | Kashmiri Rogan Josh | Aromatic lamb curry from Kashmir                       | 1\. Marinate lamb  
2\. Prepare spice paste  
3\. Slow cook with mustard oil                                                       |          1 | 2025-05-27 06:58:27 |    4.7 |  
| 52 | Sarson ka Saag      | Punjabi mustard greens curry                           | 1\. Cook greens  
2\. Prepare tempering  
3\. Serve with makki roti                                                                |          1 | 2025-05-27 06:58:27 |    4.6 |  
| 53 | Gur ki Chai         | Jaggery sweetened spiced tea                           | 1\. Boil water with spices  
2\. Add tea leaves  
3\. Sweeten with jaggery                                                         |          1 | 2025-05-27 06:58:27 |    4.3 |  
| 54 | Kashmiri Dum Aloo   | Baby potatoes in yogurt gravy                          | 1\. Fry potatoes  
2\. Prepare gravy  
3\. Dum cook                                                                                |          1 | 2025-05-27 06:58:27 |    4.5 |  
| 55 | Bathua Raita        | Chenopodium yogurt dip                                 | 1\. Blanch bathua  
2\. Mix with yogurt  
3\. Add tempering                                                                        |          1 | 2025-05-27 06:58:27 |    4.2 |  
| 56 | Pesarattu           | Green moong dal dosa                                   | 1\. Soak moong dal  
2\. Grind to batter  
3\. Cook like dosa                                                                      |          1 | 2025-05-27 06:58:27 |    4.4 |  
| 57 | Uppu Pindi          | Andhra spicy rice flour snack                          | 1\. Mix dry ingredients  
2\. Steam cook  
3\. Cut into pieces                                                                     |          1 | 2025-05-27 06:58:27 |    4.1 |  
| 58 | Kozhikode Biryani   | Malabar style dum biryani                              | 1\. Marinate chicken  
2\. Layer with rice  
3\. Dum cook                                                                          |          1 | 2025-05-27 06:58:27 |    4.8 |  
| 59 | Kootu Curry         | Kerala vegetable stew with coconut                     | 1\. Cook vegetables  
2\. Add coconut paste  
3\. Temper                                                                           |          1 | 2025-05-27 06:58:27 |    4.3 |  
| 60 | Neer Dosa           | Mangalorean watery rice crepe                          | 1\. Soak rice  
2\. Grind to watery batter  
3\. Cook on tawa                                                                      |          1 | 2025-05-27 06:58:27 |    4.2 |  
| 61 | Muri Ghonto         | Bengali fish head with rice                            | 1\. Fry fish head  
2\. Cook with rice  
3\. Add spices                                                                            |          1 | 2025-05-27 06:58:27 |    4.5 |  
| 62 | Chakuli Pitha       | Odisha rice flour pancakes                             | 1\. Prepare batter  
2\. Ferment  
3\. Cook on griddle                                                                             |          1 | 2025-05-27 06:58:27 |      4 |  
| 63 | Til ki Chutney      | Sesame seed chutney from Bihar                         | 1\. Roast sesame  
2\. Grind with spices  
3\. Mix with water                                                                      |          1 | 2025-05-27 06:58:27 |    4.1 |  
| 64 | Komdi Cha Rassa     | Maharashtrian chicken curry                            | 1\. Marinate chicken  
2\. Prepare coconut gravy  
3\. Cook together                                                               |          1 | 2025-05-27 06:58:27 |    4.6 |  
| 65 | Patishapta          | Bengali rice flour crepes with coconut-jaggery filling | 1\. Prepare batter  
2\. Make filling  
3\. Roll crepes                                                                            |          1 | 2025-05-27 06:58:27 |    4.7 |  
| 66 | Sabudana Khichdi    | Maharashtrian fasting dish                             | 1\. Soak sago  
2\. Temper spices  
3\. Cook with peanuts                                                                          |          1 | 2025-05-27 06:58:27 |    4.3 |  
| 67 | Thecha              | Maharashtrian spicy chutney                            | 1\. Pound chilies-garlic  
2\. Add crushed peanuts  
3\. Temper                                                                    |          1 | 2025-05-27 06:58:27 |    4.2 |  
| 68 | Kaju Katli          | Cashew fudge from Gujarat                              | 1\. Grind cashews  
2\. Cook with sugar  
3\. Set and cut                                                                          |          1 | 2025-05-27 06:58:27 |    4.9 |  
| 69 | Ghavan              | Konkan rice flour pancakes                             | 1\. Prepare batter  
2\. Cook like dosa  
3\. Serve with chutney                                                                   |          1 | 2025-05-27 06:58:27 |      4 |  
| 70 | Basundi             | Gujarati thickened milk dessert                        | 1\. Boil milk  
2\. Reduce with sugar  
3\. Add nuts                                                                               |          1 | 2025-05-27 06:58:27 |    4.8 |  
| 71 | Tofu Tikka Masala   | Creamy tomato-based curry with marinated tofu          | 1\. Press and cube tofu  
2\. Marinate in yogurt and spices  
3\. Grill or bake tofu  
4\. Prepare masala gravy  
5\. Combine and simmer |          1 | 2025-05-27 07:13:04 |    4.5 |  
| 73 | Tofu Bhurji         | Indian-style scrambled tofu with spices                | 1\. Crumble tofu  
2\. Saute onions and spices  
3\. Add tofu and cook  
4\. Garnish with coriander                                   |          1 | 2025-05-27 07:15:30 |    4.2 |  
\+----+---------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------+---------------------+--------+  
72 rows in set (0.001 sec)  
mysql\> mysql\> SELECT \* FROM submitted\_recipes;  
Empty set (0.003 sec)  
mysql\> SELECT \* FROM users;  
\+----+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+  
| id | username  | password\_hash                                                                                                                                                      | created\_at          |  
\+----+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+  
|  1 | admin     | hashedpassword                                                                                                                                                     | 2025-05-04 18:54:46 |  
|  2 | Nivi      | scrypt:32768:8:1$AnHu0JG582yEz4Ao$5d162bbe9ca5a5e0ceb3b5786613e2019fa7b48582d7eea7cad000cbf38fc9129a1714eb62de5639a45ceab93a389643f539cbf9de88792e87725262c13ef95d | 2025-05-04 20:00:43 |  
|  3 | Harshini  | scrypt:32768:8:1$JhQnEqRYIS1uYCXF$913013f795dd3d16cd243c83a88cddefec111f75e1ba6baf0cc775485a2660506d4a1322f53bb69836575f6c1cb4cca7793c0ee1c073172c69eb77f745b4774c | 2025-05-06 13:24:41 |  
|  9 | nivi123   | scrypt:32768:8:1$fXoOOQVMLd0NasDG$36ae847e85831a9a5467d4183fab441e61e6283d9d37575d54192c3dc8c1e2912cc06f2c937226aa4d7b15343c7abf811ec356e36b1ca6c66b3336ad0f32e790 | 2025-05-24 18:05:19 |  
| 10 | Niveditha | scrypt:32768:8:1$GwhykuhrmanObJo5$27e18f5c493f5f839c27ab19f29c1162cfc7d6590897cdc59021857a91122880eff1a36c4c1b0933da0174185ad44161d4589589ebef84ef31f9bd1da2caa436 | 2025-05-27 06:42:13 |  
\+----+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+  
5 rows in set (0.003 sec)  
mysql\>   
