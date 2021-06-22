

class Basket():
    """
    a base basket class, providing some default behaviors that can be inherited or overrided
    , as necessary. 
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number':123456}
        self.basket = basket
         