with open("data/data_metro_dehli.txt", "r") as file:
    data_nodes = {} # prepared data for analisis

    for line in file:
        station_1, station_2, distance = line.split(",")
        distance = float(distance)
        
        # create the going direction of the node
        if station_1 not in data_nodes.keys():
            data_nodes[station_1] = {station_2: distance} # key: station_1 --> value: {"station_2": cost}
        
        else:
            data_nodes[station_1].update({station_2: distance}) # key: station_1 --> value: {"station_2": cost, "station_x": cost, ...}

        # create the returning direction of the node
        if station_2 not in data_nodes.keys():
            data_nodes[station_2] = {station_1: distance} 

        else:
            data_nodes[station_2].update({station_1: distance})
    
