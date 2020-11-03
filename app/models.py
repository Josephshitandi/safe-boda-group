class Book(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    rider_name = db.Column(db.String(255), index=True)
    first_point = db.Column(db.String(255), index=True)
    second_point = db.Column(db.String(255), index=True)
    payment = db.Column(db.String(255), index=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    rider_id = db.Column(db.Integer, db.ForeignKey('riders.id'), nullable=False)

    

    def save_booking(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_bookings(cls, id):
        bookings = Book.query.filter_by(id=id).all()
        return bookings

    @classmethod
    def get_all_bookings(cls):
        bookings = Book.query.order_by('-id').all()
        return bookings

    def __repr__(self):
        return f'Bookings {self._title}'