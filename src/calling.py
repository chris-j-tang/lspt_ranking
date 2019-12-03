import json

import falcon
from initial_design import GET

CORRECT_REQUEST = """Error request format. The request must contain query=[string].
Optional fields include n_results = int"""

class Resource(object):

    def on_get(self, req, resp):
        # Extract the query and fields from the request.
        to_rank = json.loads(req.params.get('query', '[]'))
        n_results = req.params.get('n_results', 50)

        # Check that the query is well-formed.
        print(to_rank)
        if to_rank == [] or \
            not isinstance(to_rank, list) or \
            any(not isinstance(s, str) for s in to_rank):
            resp.body = CORRECT_REQUEST
            resp.status = falcon.HTTP_400
        else:
            results = GET(to_rank, n_results=n_results)

            # Create a JSON representation of the resource.
            resp.body = json.dumps(results, ensure_ascii=False)

            resp.status = falcon.HTTP_200
