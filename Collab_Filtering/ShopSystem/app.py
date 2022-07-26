from flask import Flask, request,jsonify
import json
import read_data_func
import collab_filtering

app = Flask(__name__)

@app.route("/api/collab-filtering/<int:ids>", methods=['GET'])
def face_recognition(ids):
	# data = request.get_json()
	# data = data['input']
	data_matrix = read_data_func.get_dataframe_views_base('ub.base')
	cf_rs = collab_filtering.CF(data_matrix, k=2, uuCF=1)
	cf_rs.fit()
	result = cf_rs.recommend_top(ids, top_x=2)
	output = json.dumps(result)
	return output

if __name__ == '__main__':
	app.run()