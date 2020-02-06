from pyramid.view import view_config
import pyramid.httpexceptions as exc
from ..scripts.utils import Utils
from ..models import Constant
import transaction

from sqlalchemy.exc import DBAPIError
from ..exceptions.custom_error import CustomError

from .. import models

import logging
log = logging.getLogger(__name__)


###########################################################
# EMOLUMENTS
###########################################################

""" Return all emoluments in facture"""
@view_config(route_name='facture_emoluments_by_facture_id', request_method='GET', renderer='json')
def facture_emoluments_view(request):
    facture_id = request.matchdict["id"]

    try:
        query = request.dbsession.query(models.VEmolumentsFactures)\
            .filter(models.VEmolumentsFactures.facture_id == facture_id).all()
        return Utils.serialize_many(query)

    except DBAPIError as e:
        log.error(e)
        return exc.HTTPBadRequest(e)


""" Add new emolument_facture"""
@view_config(route_name='emolument_facture', request_method='POST', renderer='json')
@view_config(route_name='emolument_facture_s', request_method='POST', renderer='json')
def emolument_facture_new_view(request):

    record = models.EmolumentFacture()
    record = Utils.set_model_record(record, request.params)

    try:
        with transaction.manager:
            request.dbsession.add(record)
            transaction.commit()
            return Utils.get_data_save_response(Constant.SUCCESS_SAVE.format(models.EmolumentFacture.__tablename__))

    except DBAPIError as e:
        log.error(e)
        return exc.HTTPBadRequest(e)


""" Update emolument_facture"""
@view_config(route_name='emolument_facture', request_method='PUT', renderer='json')
@view_config(route_name='emolument_facture_s', request_method='PUT', renderer='json')
def emolument_facture_update_view(request):
    emolument_facture_id = request.params['id'] if 'id' in request.params else None

    # Get the facture
    record = request.dbsession.query(models.EmolumentFacture).filter(
        models.EmolumentFacture.id == emolument_facture_id).first()

    if not record:
        raise CustomError(
            CustomError.RECORD_WITH_ID_NOT_FOUND.format(models.EmolumentFacture.__tablename__, emolument_facture_id))

    record = Utils.set_model_record(record, request.params)

    try:
        with transaction.manager:
            transaction.commit()
            return Utils.get_data_save_response(Constant.SUCCESS_SAVE.format(models.EmolumentFacture.__tablename__))

    except DBAPIError as e:
        log.error(e)
        return exc.HTTPBadRequest(e)


""" Delete emolument_facture"""
@view_config(route_name='emolument_facture_by_id', request_method='DELETE', renderer='json')
def emolument_facture_delete_view(request):
    try:
        id = request.matchdict['id']

        record = request.dbsession.query(models.EmolumentFacture).filter(
            models.EmolumentFacture.id == id).first()

        if not record:
            raise CustomError(
                CustomError.RECORD_WITH_ID_NOT_FOUND.format(models.EmolumentFacture.__tablename__, id))

        with transaction.manager:
            request.dbsession.delete(record)
            transaction.commit()
            return Utils.get_data_save_response(Constant.SUCCESS_DELETE.format(models.EmolumentFacture.__tablename__))

    except DBAPIError as e:
        log.error(e)
        return exc.HTTPBadRequest(e)