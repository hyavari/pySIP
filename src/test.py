import textwrap
import json
from sip_message import SipMessage
def prepare_msg(msg: str):
    # Message lines must be CRLF-terminated and not indented
    return textwrap.dedent(msg).replace("\n", "\r\n")

invite = """\
        INVITE sip:18259990275;phone-context=ims.mnc221.mcc302.3gppnetwork.org@ims.mnc221.mcc302.3gppnetwork.org;user=phone SIP/2.0
        Via: SIP/2.0/TCP [2001:56b:f:538:0:3a:b637:c001]:7200;branch=z9hG4bK-524287-1---1800cdbc7db6881f;rport;transport=TCP
        Max-Forwards: 70
        Route: <sip:[2001:56b:f:538:0:3a:b637:c001]:12003;lr>
        Proxy-Require: sec-agree
        Require: sec-agree
        Contact: <sip:18259990284@[2001:56b:f:538:0:3a:b637:c001]:7200>;+sip.instance="<urn:gsma:imei:35269610-004503-0>";+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel";+g.3gpp.mid-call;+g.3gpp.srvcc-alerting;+g.3gpp.ps2cs-srvcc-orig-pre-alerting
        To: <sip:18259990275;phone-context=ims.mnc221.mcc302.3gppnetwork.org@ims.mnc221.mcc302.3gppnetwork.org;user=phone>
        From: <sip:18259990284@ims.mnc221.mcc302.3gppnetwork.org>;tag=79877031
        Call-ID: WJW0YkVy1vkpwJsITEw_gw..@2001:56b:f:538:0:3a:b637:c001
        CSeq: 1 INVITE
        Session-Expires: 1800
        Accept: application/sdp, application/3gpp-ims+xml
        Allow: INVITE, ACK, OPTIONS, CANCEL, BYE, UPDATE, INFO, REFER, NOTIFY, MESSAGE, PRACK
        Content-Type: application/sdp
        Supported: timer, 100rel, precondition, gruu, sec-agree
        User-Agent: SM-G975W-G975WVLS5GUD1 6.0
        Security-Verify: ipsec-3gpp;prot=esp;mod=trans;spi-c=12002;spi-s=12003;port-c=12002;port-s=12003;alg=hmac-sha-1-96;ealg=null
        P-Preferred-Identity: <sip:18259990284@ims.mnc221.mcc302.3gppnetwork.org>
        Accept-Contact: *;+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel"
        P-Early-Media: supported
        P-Preferred-Service: urn:urn-7:3gpp-service.ims.icsi.mmtel
        P-Access-Network-Info: 3GPP-E-UTRAN-FDD;utran-cell-id-3gpp=3022202b081b15848
        History-Info: <sip:302221004624159@ims.mnc221.mcc302.3gppnetwork.org>;index=1
        History-Info: <sip:302221004624159@ims.mnc221.mcc302.3gppnetwork.org>;index=1.1
        Content-Length: 914

        v=0
        o=SAMSUNG-IMS-UE 31258835364 31258835364 IN IP6 2001:56b:f:538:0:3a:b637:c001
        s=SS VOIP
        c=IN IP6 2001:56b:f:538:0:3a:b637:c001
        t=0 0
        m=audio 1314 RTP/AVP 127 116 107 118 96 111 110
        b=AS:50
        b=RS:0
        b=RR:2500
        a=rtpmap:127 EVS/16000
        a=fmtp:127 br=5.9-24.4;bw=nb-swb;ch-aw-recv=2
        a=rtpmap:116 AMR-WB/16000/1
        a=fmtp:116 mode-set=0,1,2;mode-change-capability=2;max-red=220
        a=rtpmap:107 AMR-WB/16000/1
        a=fmtp:107 mode-set=0,1,2;octet-align=1;mode-change-capability=2;max-red=220
        a=rtpmap:118 AMR/8000/1
        a=fmtp:118 mode-change-capability=2;max-red=220
        a=rtpmap:96 AMR/8000/1
        a=fmtp:96 octet-align=1;mode-change-capability=2;max-red=220
        a=rtpmap:111 telephone-event/16000
        a=fmtp:111 0-15
        a=rtpmap:110 telephone-event/8000
        a=fmtp:110 0-15
        a=curr:qos local none
        a=curr:qos remote none
        a=des:qos mandatory local sendrecv
        a=des:qos optional remote sendrecv
        a=sendrecv
        a=ptime:20
        a=maxptime:240

        """

register = """\
        REGISTER sip:ims.mnc221.mcc302.3gppnetwork.org SIP/2.0
        Via: SIP/2.0/TCP [2001:56b:f:628:0:4a:634d:2701]:8800;branch=z9hG4bK-524287-1---ad3f1d8b12f767df;rport;transport=TCP
        Max-Forwards: 70
        Proxy-Require: sec-agree
        Require: sec-agree
        Contact: <sip:302221004624159@192.168.1.10:8800>;+sip.instance="<urn:gsma:imei:35269610-004587-0>";q=1.0;+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel";+g.3gpp.smsip
        To: <sip:302221004624159@ims.mnc221.mcc302.3gppnetwork.org>
        From: <sip:302221004624159@ims.mnc221.mcc302.3gppnetwork.org>;tag=266fb219
        Call-ID: ogkd1rXUCrVzCzJAyYqHhg..@2001:56b:f:628:0:4a:634d:2701
        CSeq: 6 REGISTER
        Expires: 3600
        Allow: INVITE, ACK, OPTIONS, CANCEL, BYE, UPDATE, INFO, REFER, NOTIFY, MESSAGE, PRACK
        Supported: path, gruu, sec-agree
        User-Agent: SM-G975W-G975WVLU4FUA2 6.0
        Authorization: Digest username="302221004624159@ims.mnc221.mcc302.3gppnetwork.org",realm="ims.mnc221.mcc302.3gppnetwork.org",uri="sip:ims.mnc221.mcc302.3gppnetwork.org",nonce="kl+Oj3dVBnPeJ81IgWQ3o5qRg0vRLAAAddzrHJfngh8=",response="f225271605224d9b278acd9ab4beccc0",algorithm=AKAv1-MD5,nc=00000005,qop=auth,cnonce="7c1ef4f230d371bafa78fa2dfc6ef84d"
        Security-Client: ipsec-3gpp;prot=esp;mod=trans;spi-c=73111;spi-s=73112;port-c=8802;port-s=8800;alg=hmac-md5-96;ealg=null, ipsec-3gpp;prot=esp;mod=trans;spi-c=73111;spi-s=73112;port-c=8802;port-s=8800;alg=hmac-sha-1-96;ealg=null
        Security-Verify: ipsec-3gpp;prot=esp;mod=trans;spi-c=12008;spi-s=12009;port-c=12008;port-s=12009;alg=hmac-sha-1-96;ealg=null
        P-Access-Network-Info: 3GPP-E-UTRAN-FDD;utran-cell-id-3gpp=302220d6dd8683a2a
        Content-Length: 0

        """

        
original_message = prepare_msg(invite)
sip_msg = SipMessage.from_string(original_message)

print(json.dumps(sip_msg.headers))