from ridemyway.models.ride import Ride
from datetime import datetime
from flask import current_app as app


class RideController():
    """
        Controls all CRUD operations of the Ride object.
    """

    def create_ride(self, **Kwargs):
        """
            Creates and adds a ride to the app database.

            Returns:
                A success status if success adding ride,
                failed status otherwise.
        """
        try:
            ride_ids = [x for x in app.database['Rides']]
            if ride_ids:
                ride_id = max(ride_ids) + 1
            else:
                ride_id = 1
            date_offered = datetime.now().strftime('%b %d %Y %H:%M%p')
            self.new_ride = Ride(
                                ride_id=ride_id,
                                departure=Kwargs['departure'],
                                origin=Kwargs['origin'],
                                destination=Kwargs['destination'],
                                vehicle_number_plate=
                                Kwargs['vehicle_number_plate'],
                                capacity=Kwargs['capacity'],
                                cost=Kwargs['cost'],
                                date_offered=date_offered,
                                availability='available')
            ride = self.new_ride.__dict__
            app.database['Rides'][self.new_ride.ride_id] = ride
            status = {
                  'status': 'success',
                  'message': 'Ride created successfully',
                  'attributes': {
                      'location':
                      '/api/v1/rides/' + str(ride['ride_id']),
                      'repr':
                      str(ride['ride_id']) + ' - from ' +
                      ride['origin'] + ' to ' +
                      ride['destination']
                      }
                }
            return(status)
        except Exception as e:
            status = {
                'status': 'failed',
                'message': 'Exceptions',
                'meta': {
                    'errors': 1
                    },
                'errors': [
                    {
                        str(type(e)): str(e)
                        }
                    ]
                }
            return(status)