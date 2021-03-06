# -*- coding: utf-8 -*-

import inventree.base
import inventree.order


class Company(inventree.base.InventreeObject):
    """ Class representing the Company database model """

    URL = 'company'

    def getSuppliedParts(self, **kwargs):
        """
        Return list of SupplierPart objects supplied by this Company
        """
        return SupplierPart.list(self._api, supplier=self.pk, **kwargs)

    def getManufacturedParts(self, **kwargs):
        """
        Return list of ManufacturerPart objects manufactured by this Company
        """
        return ManufacturerPart.list(self._api, manufacturer=self.pk, **kwargs)

    def getPurchaseOrders(self, **kwargs):
        """
        Return list of PurchaseOrder objects associated with this company
        """
        return inventree.order.PurchaseOrder.list(self._api, supplier=self.pk)

    def createPurchaseOrder(self, **kwargs):
        """
        Create (and return) a new PurchaseOrder against this company
        """

        kwargs['supplier'] = self.pk

        return inventree.order.PurchaseOrder.create(
            self._api,
            data=kwargs
        )

    def getSalesOrders(self, **kwargs):
        """
        Return list of SalesOrder objects associated with this company
        """
        return inventree.order.SalesOrder.list(self._api, customer=self.pk)

    def createSalesOrder(self, **kwargs):
        """
        Create (and return) a new SalesOrder against this company
        """

        kwargs['customer'] = self.pk

        return inventree.order.SalesOrder.create(
            self._api,
            data=kwargs
        )


class SupplierPart(inventree.base.InventreeObject):
    """ Class representing the SupplierPart database model """

    URL = 'company/part'

    def getPriceBreaks(self):
        """ Get a list of price break objects for this SupplierPart """

        return SupplierPriceBreak.list(self._api, part=self.pk)


class ManufacturerPart(inventree.base.InventreeObject):
    """
    Class representing the ManufacturerPart database model
    """

    URL = 'company/part/manufacturer'

    def getParameters(self, **kwargs):
        """
        GET a list of all ManufacturerPartParameter objects for this ManufacturerPart
        """

        return ManufacturerPartParameter.list(self._api, manufacturer_part=self.pk, **kwargs)


class ManufacturerPartParameter(inventree.base.InventreeObject):
    """
    Class representing the ManufacturerPartParameter database model.
    """

    URL = 'company/part/manufacturer/parameter'


class SupplierPriceBreak(inventree.base.InventreeObject):
    """ Class representing the SupplierPriceBreak database model """

    URL = 'company/price-break'
