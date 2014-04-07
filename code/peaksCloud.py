__author__ = 'mariosky'

import ppeaks, random_ppeaks
import cloud, time, yaml


config = yaml.load(open("conf/conf.yaml"))

experiment = "w%d-%d-p%d" % (config["NUMBER_OF_WORKERS"], config["RETURN_RATE"]*100,config["POPULATION_SIZE"])
experiment_id = experiment + "-%d" % round(time.time(),0)

datafile = open(experiment_id+".dat","a")
conf_out = open("conf/"+experiment_id+".yaml","w")
yaml.dump(config, conf_out)
conf_out.close()

for i in range(1):
    start = time.time()
    init_job = cloud.call(ppeaks.initialize, config=config,  _type=config["WORKER_TYPE"], _env="deap")
    tInitialize = time.time()-start
    print i, tInitialize
    params = [(w, config) for w in range(config["NUMBER_OF_WORKERS"])]

    jids = cloud.map(ppeaks.work, params, _type=config["WORKER_TYPE"], _depends_on= init_job )
    results_list = cloud.result(jids)

    tTotal = time.time()-start
    totals = "%d,%0.2f,%0.2f" % (i, round(tTotal,2), round(tInitialize,2))
    print totals
    datafile.write(totals + '\n')
    for worker_list in results_list:
        for data_list in worker_list:
            datafile.write(str(i) +"," + ",".join(map(str,data_list)) + '\n')

