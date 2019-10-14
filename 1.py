import requests

INF = 1000
#zhuyan guo

au_n = input()
au_f = input()
au_name = au_n + '+' + au_f
link = 'https://api.crossref.org/works?query.author=' + au_name + '&rows=800'
t = requests.get(link).json()
wl = t['message']['items']

co_auth = {}
co_auth_conc = []
#for i in range (INF):
#        co_auth_conc[i] = [0] * INF
for i in range (INF):
    f = []
    co_auth_conc.append([])
    for j in range (INF):
        f.append(0)
        co_auth_conc[i].append(0)
    #co_auth_conc[i].append(f)
co_auth_num = {}
num_co_auth = {}

i = 1
cnt = 0
for w in wl:
    i+=1
    #if (i < 100):
        #print (w.keys())
    wk = list(w.keys()).copy()
    if 'author' in wk:
        auths = list(w['author']).copy()
        if len(auths) > 1:
            #print (w['author'])
            cur_auths = []
            for a in auths:
                print (a.keys())
                if ('family' in a.keys()) and (a['family'] != ):
                    if (co_auth.get(a['family']) == None):
                        co_auth[a['family']] = 1
                        co_auth_num[a['family']] = cnt
                        num_co_auth[cnt] = a['family']
                        cnt += 1
                    else:
                        co_auth[a['family']] += 1
                    cur_auths.append(co_auth_num[a['family']])
                    for n in cur_auths:
                        co_auth_conc[n][co_auth_num[a['family']]] = co_auth_conc[n][co_auth_num[a['family']]] + 1
                        co_auth_conc[co_auth_num[a['family']]][n] += 1

co_auth_k = list(co_auth.keys())

labs = []

for a1 in range (cnt):
    labs.append([])
    for a2 in range (cnt):
        if a1 != a2:
            if ((co_auth[num_co_auth[a1]] > 3) and (co_auth[num_co_auth[a2]] > 3)
                        and (co_auth_conc[a1][a2] * 5 / 4 > min(co_auth[num_co_auth[a1]], co_auth[num_co_auth[a2]]))):
                labs[a1].append(a2)

for a1 in range (j):
    if (len(labs[a1]) > 0):
        for a_id in labs[a1]:
            print (num_co_auth[a_id], co_auth[num_co_auth[a_id]])
        print("///")