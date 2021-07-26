from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='sogang-register related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
    })
    # 새로운 user의 email 인증과 관련해서 request를 email, access code 두 개로 하려고 하는데 괜찮겠지?
    user_verify = api.model('user_verify', {
        'email': fields.String(required=True, description='user email address'),
        'access_code': fields.String(required=True, description='access code sent to user email'),
    })
    
class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
    
class SearchDto:
    api = Namespace('search', description='db search related operations')
    subject = api.model('subject', {
        '학년도': fields.String(required=True, description='test'),
        '학기': fields.String(required=True, description='test'),
        '소속': fields.String(required=True, description='test'),
        '학과': fields.String(required=True, description='test'),
        '과목번호': fields.String(required=True, description='test'),
        '분반': fields.String(required=True, description='test'),
        '과목명': fields.String(required=True, description='test'),
        '강의계획서': fields.String(required=True, description='test'),
        '학점': fields.String(required=True, description='test'),
        '수업시간_강의실': fields.String(required=True, description='test'),
        '시간': fields.String(required=True, description='test'),
        '교수진': fields.String(required=True, description='test'),
        '수강생수': fields.String(required=True, description='test'),
        '영어강의': fields.String(required=True, description='test'),
        '중국어강의': fields.String(required=True, description='test'),
        '공학인증': fields.String(required=True, description='test'),
        '국제학생': fields.String(required=True, description='test'),
        'Honors과목': fields.String(required=True, description='test'),
        '홀짝구분': fields.String(required=True, description='test'),
        '승인과목': fields.String(required=True, description='test'),
        '시험일자': fields.String(required=True, description='test'),
        '수강대상': fields.String(required=True, description='test'),
        '권장학년': fields.String(required=True, description='test'),
        '수강신청_참조사항': fields.String(required=True, description='test'),
        '과목_설명': fields.String(required=True, description='test'),
        '비고': fields.String(required=True, description='test'),
        'subject_id' : fields.String(required=True, description='test'),
        '전인교육원' : fields.String(required=True, description='test')
    })
    
