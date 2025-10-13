import urllib.parse

def build_upi_deeplink(payee_vpa, payee_name, amount, txn_id=None, note=None, currency='INR'):
    """
    Construct an UPI deeplink like:
    upi://pay?pa=merchant@upi&pn=MerchantName&am=10.00&cu=INR&tn=Order+123
    """
    params = {
        'pa': payee_vpa,
        'pn': payee_name,
        'am': f"{amount:.2f}",
        'cu': currency,
    }
    if txn_id:
        params['tr'] = str(txn_id)  # merchant transaction reference (optional)
    if note:
        params['tn'] = note

    query = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    return f"upi://pay?{query}"