from flask import Flask, request
app = Flask(__name__)

@app.route('/address/exposure/direct',  methods=['GET'])
def address_exposure_direct():
  address  = request.args.get('address', '')
  start_date = request.args.get('start_date', '0001-01-01T00:00:00Z')
  end_date = request.args.get('end_date', '9999-12-31T23:59:59Z')
  flow_type = request.args.get('flow_type', 'both')
  limit = request.args.get('limit', 100)
  offset = request.args.get('offset', 0)

  sample_res = { "data": [ { "address": address, "inflows": "", "outflows": "", "total_flows": "" } ], "success": True }

  return sample_res 
