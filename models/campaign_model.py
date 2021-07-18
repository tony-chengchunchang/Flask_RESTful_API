from db import db

class CampaignModel(db.Model):
    __tablename__ = 'campaign_target'
    account_id = db.Column(db.BigInteger)
    campaign_id = db.Column(db.BigInteger(), primary_key=True)
    destination_type = db.Column(db.Text)
    destination = db.Column(db.Integer)

    def __init__(self, account_id, campaign_id, destination_type, destination):
        self.account_id = account_id
        self.campaign_id = campaign_id
        self.destination_type = destination_type
        self.destination = destination

    def json(self):
        return {
            'account_id': self.account_id,
            'campaign_id': self.campaign_id,
            'destination_type': self.destination_type,
            'destination': self.destination
        }

    @classmethod
    def get_one_campaign(cls, campaign_id):
        return cls.query.filter_by(campaign_id=campaign_id).first()

    # @classmethod
    # def get_all_campaigns(cls):
    #     campaign_list = [c.json() for c in cls.query.all()]
    #     return {'campaigns': campaign_list}

    def upsert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
