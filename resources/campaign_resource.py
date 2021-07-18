from flask_restful import Resource
from flask_restful import reqparse
from models.campaign_model import CampaignModel

class Campaign(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('account_id', type=int)
    parser.add_argument('destination_type', type=str)
    parser.add_argument('destination', type=int)

    def get(self, campaign_id):
        campaign = CampaignModel.get_one_campaign(campaign_id)
        if campaign:
            return campaign.json(), 200

        return {'message': 'Campaign not found'}, 404

    def post(self, campaign_id):
        campaign = CampaignModel.get_one_campaign(campaign_id)
        if campaign:
            return {'message': 'Campaign already exists'}, 400

        data = self.parser.parse_args()
        campaign = CampaignModel(campaign_id=campaign_id, **data)
        try:
            campaign.upsert()
            return campaign.json(), 201
        except:
            return {'message': 'Internal Error'}, 500

    def put(self, campaign_id):
        data = self.parser.parse_args()

        campaign = CampaignModel.get_one_campaign(campaign_id)
        if campaign:
            campaign.destination_type = data['destination_type']
            campaign.destination = data['destination']
        else:
            campaign = CampaignModel(campaign_id=campaign_id, **data)

        campaign.upsert()

        return campaign.json(), 200

    def delete(self, campaign_id):
        campaign = CampaignModel.get_one_campaign(campaign_id)
        if campaign:
            campaign.delete()

        return {'message': 'Campaign Deleted'}
