from flask import jsonify


def GenerateResponse(data, msg):
    response_data = {}
    data_list = []
    try:
        for i in data:
            data_ins = {}
            data_ins["ord_id"] = i[0]
            data_ins["piz_type"] = i[1]
            data_ins["piz_size"] = i[2]
            data_ins["cust_phn"]=i[3]
            data_ins["cust_addr"]=i[4]
            data_ins["status"]=i[5]
            data_list.append(data_ins)
            response_data["data"] = data_list

        response_data["msg"] = msg
        print(f"Respone data : {response_data}")
        return jsonify(response_data)
    except IndexError as e:
        print(e)
        return str(e)

