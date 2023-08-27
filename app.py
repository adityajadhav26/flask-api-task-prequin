from flask import Flask, request, jsonify
import random
import logging
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from flask_caching import Cache

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['RESTX_MASK_SWAGGER'] = False  # Disable trailing slashes in Swagger UI

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

api = Api(app, version='1.0', title='Random Vector API', description='Generate a random 500-dimensional vector')

namespace = api.namespace('v1/random_vector', description='Random vector operations')

random_vector_model = api.model('RandomVector', {
    'sentence': fields.String(required=True, description='Input sentence')
})

class RandomVectorResource(Resource):
    @api.expect(random_vector_model)
    def post(self):
        try:
            data = request.json
            sentence = data['sentence']

            # Logging
            logging.info(f'Received request for sentence: {sentence}')

            # Generate a random 500-dimensional array of floats
            random_vector = [random.uniform(0, 1) for _ in range(500)]

            return random_vector, 200

        except Exception as e:
            logging.error(f'Error processing request: {e}')
            return {'error': 'An error occurred'}, 500

namespace.add_resource(RandomVectorResource, '/')

@app.route('/cached_random_vector', methods=['GET'])
@cache.cached(timeout=300)  # Cache for 5 minutes
def get_cached_random_vector():
    # Generate a random 500-dimensional array of floats
    random_vector = [random.uniform(0, 1) for _ in range(500)]
    return jsonify(random_vector), 200

if __name__ == '__main__':
    app.run(debug=True)
