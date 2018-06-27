"""
    Flask RestFul resources
"""


from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token,
                                create_refresh_token, jwt_required,
                                get_jwt_identity, get_raw_jwt)
from flask import current_app as app
import json
from ridemyway.controllers.ride_controller import RideController
from ridemyway.controllers.ride_request_controller import RequestController

from .utils import errors


rides = RideController()
ride_requests = RequestController()


class Rides(Resource):
    """
        Rides Resource
    """

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('departure',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('origin',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('destination',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('cost',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('vehicle_number_plate',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('capacity',
                                 help='This field cannot be blank',
                                 required=True)

    def post(self):
        """
            Creates a ride
        """
        data = self.parser.parse_args()
        create_ride_errors = errors.create_ride(**data)
        if create_ride_errors:
            return json.loads(json.dumps(create_ride_errors)), 400
        self.response = rides.create_ride(**data)
        return self.response, 201

    def get(self):
        """
            Fetches all rides
        """
        fetched_rides = rides.fetch_all()
        return(fetched_rides), 200


class Ride(Resource):
    """
        Ride Resource
    """

    def __init__(self):
        pass

    def get(self, rideId):
        """
            Fetches a single ride
        """
        return rides.fetch_one(rideId)


class Request(Resource):
    """
        Request resource
    """

    def __init__(self):
        pass

    def post(self, rideId):
        """
            Creates a ride request
        """
        return ride_requests.create_request(ride_id=rideId)


class All(Resource):
    """
        All Resource
    """

    def __init__(self):
        pass

    def get(self):
        """
            Returns:
                All database items
        """

        return {'message': 'all'}, 201
