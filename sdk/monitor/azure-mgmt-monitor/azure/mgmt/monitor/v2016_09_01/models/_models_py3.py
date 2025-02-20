# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ErrorResponse(_serialization.Model):
    """Describes the format of Error response.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, code: Optional[str] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword code: Error code.
        :paramtype code: str
        :keyword message: Error message indicating why the operation failed.
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message


class LocalizableString(_serialization.Model):
    """The localizable string class.

    All required parameters must be populated in order to send to Azure.

    :ivar value: the invariant value. Required.
    :vartype value: str
    :ivar localized_value: the locale specific value.
    :vartype localized_value: str
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "str"},
        "localized_value": {"key": "localizedValue", "type": "str"},
    }

    def __init__(self, *, value: str, localized_value: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword value: the invariant value. Required.
        :paramtype value: str
        :keyword localized_value: the locale specific value.
        :paramtype localized_value: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.localized_value = localized_value


class LogSettings(_serialization.Model):
    """Part of MultiTenantDiagnosticSettings. Specifies the settings for a particular log.

    All required parameters must be populated in order to send to Azure.

    :ivar category: Name of a Diagnostic Log category for a resource type this setting is applied
     to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET
     diagnostic settings operation.
    :vartype category: str
    :ivar enabled: a value indicating whether this log is enabled. Required.
    :vartype enabled: bool
    :ivar retention_policy: the retention policy for this log.
    :vartype retention_policy: ~$(python-base-namespace).v2016_09_01.models.RetentionPolicy
    """

    _validation = {
        "enabled": {"required": True},
    }

    _attribute_map = {
        "category": {"key": "category", "type": "str"},
        "enabled": {"key": "enabled", "type": "bool"},
        "retention_policy": {"key": "retentionPolicy", "type": "RetentionPolicy"},
    }

    def __init__(
        self,
        *,
        enabled: bool,
        category: Optional[str] = None,
        retention_policy: Optional["_models.RetentionPolicy"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword category: Name of a Diagnostic Log category for a resource type this setting is
         applied to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET
         diagnostic settings operation.
        :paramtype category: str
        :keyword enabled: a value indicating whether this log is enabled. Required.
        :paramtype enabled: bool
        :keyword retention_policy: the retention policy for this log.
        :paramtype retention_policy: ~$(python-base-namespace).v2016_09_01.models.RetentionPolicy
        """
        super().__init__(**kwargs)
        self.category = category
        self.enabled = enabled
        self.retention_policy = retention_policy


class Metric(_serialization.Model):
    """A set of metric values in a time range.

    All required parameters must be populated in order to send to Azure.

    :ivar id: the id, resourceId, of the metric.
    :vartype id: str
    :ivar type: the resource type of the metric resource.
    :vartype type: str
    :ivar name: the name and the display name of the metric, i.e. it is localizable string.
     Required.
    :vartype name: ~$(python-base-namespace).v2016_09_01.models.LocalizableString
    :ivar unit: the unit of the metric. Required. Known values are: "Count", "Bytes", "Seconds",
     "CountPerSecond", "BytesPerSecond", "Percent", "MilliSeconds", "ByteSeconds", "Unspecified",
     "Cores", "MilliCores", "NanoCores", and "BitsPerSecond".
    :vartype unit: str or ~$(python-base-namespace).v2016_09_01.models.Unit
    :ivar data: Array of data points representing the metric values. Required.
    :vartype data: list[~$(python-base-namespace).v2016_09_01.models.MetricValue]
    """

    _validation = {
        "name": {"required": True},
        "unit": {"required": True},
        "data": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "name": {"key": "name", "type": "LocalizableString"},
        "unit": {"key": "unit", "type": "str"},
        "data": {"key": "data", "type": "[MetricValue]"},
    }

    def __init__(
        self,
        *,
        name: "_models.LocalizableString",
        unit: Union[str, "_models.Unit"],
        data: List["_models.MetricValue"],
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        type: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword id: the id, resourceId, of the metric.
        :paramtype id: str
        :keyword type: the resource type of the metric resource.
        :paramtype type: str
        :keyword name: the name and the display name of the metric, i.e. it is localizable string.
         Required.
        :paramtype name: ~$(python-base-namespace).v2016_09_01.models.LocalizableString
        :keyword unit: the unit of the metric. Required. Known values are: "Count", "Bytes", "Seconds",
         "CountPerSecond", "BytesPerSecond", "Percent", "MilliSeconds", "ByteSeconds", "Unspecified",
         "Cores", "MilliCores", "NanoCores", and "BitsPerSecond".
        :paramtype unit: str or ~$(python-base-namespace).v2016_09_01.models.Unit
        :keyword data: Array of data points representing the metric values. Required.
        :paramtype data: list[~$(python-base-namespace).v2016_09_01.models.MetricValue]
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.unit = unit
        self.data = data


class MetricCollection(_serialization.Model):
    """The collection of metric value sets.

    All required parameters must be populated in order to send to Azure.

    :ivar value: the value of the collection. Required.
    :vartype value: list[~$(python-base-namespace).v2016_09_01.models.Metric]
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Metric]"},
    }

    def __init__(self, *, value: List["_models.Metric"], **kwargs: Any) -> None:
        """
        :keyword value: the value of the collection. Required.
        :paramtype value: list[~$(python-base-namespace).v2016_09_01.models.Metric]
        """
        super().__init__(**kwargs)
        self.value = value


class MetricSettings(_serialization.Model):
    """Part of MultiTenantDiagnosticSettings. Specifies the settings for a particular metric.

    All required parameters must be populated in order to send to Azure.

    :ivar time_grain: the timegrain of the metric in ISO8601 format. Required.
    :vartype time_grain: ~datetime.timedelta
    :ivar enabled: a value indicating whether this timegrain is enabled. Required.
    :vartype enabled: bool
    :ivar retention_policy: the retention policy for this timegrain.
    :vartype retention_policy: ~$(python-base-namespace).v2016_09_01.models.RetentionPolicy
    """

    _validation = {
        "time_grain": {"required": True},
        "enabled": {"required": True},
    }

    _attribute_map = {
        "time_grain": {"key": "timeGrain", "type": "duration"},
        "enabled": {"key": "enabled", "type": "bool"},
        "retention_policy": {"key": "retentionPolicy", "type": "RetentionPolicy"},
    }

    def __init__(
        self,
        *,
        time_grain: datetime.timedelta,
        enabled: bool,
        retention_policy: Optional["_models.RetentionPolicy"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword time_grain: the timegrain of the metric in ISO8601 format. Required.
        :paramtype time_grain: ~datetime.timedelta
        :keyword enabled: a value indicating whether this timegrain is enabled. Required.
        :paramtype enabled: bool
        :keyword retention_policy: the retention policy for this timegrain.
        :paramtype retention_policy: ~$(python-base-namespace).v2016_09_01.models.RetentionPolicy
        """
        super().__init__(**kwargs)
        self.time_grain = time_grain
        self.enabled = enabled
        self.retention_policy = retention_policy


class MetricValue(_serialization.Model):
    """Represents a metric value.

    All required parameters must be populated in order to send to Azure.

    :ivar time_stamp: the timestamp for the metric value in ISO 8601 format. Required.
    :vartype time_stamp: ~datetime.datetime
    :ivar average: the average value in the time range.
    :vartype average: float
    :ivar minimum: the least value in the time range.
    :vartype minimum: float
    :ivar maximum: the greatest value in the time range.
    :vartype maximum: float
    :ivar total: the sum of all of the values in the time range.
    :vartype total: float
    :ivar count: the number of samples in the time range. Can be used to determine the number of
     values that contributed to the average value.
    :vartype count: int
    """

    _validation = {
        "time_stamp": {"required": True},
    }

    _attribute_map = {
        "time_stamp": {"key": "timeStamp", "type": "iso-8601"},
        "average": {"key": "average", "type": "float"},
        "minimum": {"key": "minimum", "type": "float"},
        "maximum": {"key": "maximum", "type": "float"},
        "total": {"key": "total", "type": "float"},
        "count": {"key": "count", "type": "int"},
    }

    def __init__(
        self,
        *,
        time_stamp: datetime.datetime,
        average: Optional[float] = None,
        minimum: Optional[float] = None,
        maximum: Optional[float] = None,
        total: Optional[float] = None,
        count: Optional[int] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword time_stamp: the timestamp for the metric value in ISO 8601 format. Required.
        :paramtype time_stamp: ~datetime.datetime
        :keyword average: the average value in the time range.
        :paramtype average: float
        :keyword minimum: the least value in the time range.
        :paramtype minimum: float
        :keyword maximum: the greatest value in the time range.
        :paramtype maximum: float
        :keyword total: the sum of all of the values in the time range.
        :paramtype total: float
        :keyword count: the number of samples in the time range. Can be used to determine the number of
         values that contributed to the average value.
        :paramtype count: int
        """
        super().__init__(**kwargs)
        self.time_stamp = time_stamp
        self.average = average
        self.minimum = minimum
        self.maximum = maximum
        self.total = total
        self.count = count


class Resource(_serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class RetentionPolicy(_serialization.Model):
    """Specifies the retention policy for the log.

    All required parameters must be populated in order to send to Azure.

    :ivar enabled: a value indicating whether the retention policy is enabled. Required.
    :vartype enabled: bool
    :ivar days: the number of days for the retention in days. A value of 0 will retain the events
     indefinitely. Required.
    :vartype days: int
    """

    _validation = {
        "enabled": {"required": True},
        "days": {"required": True, "minimum": 0},
    }

    _attribute_map = {
        "enabled": {"key": "enabled", "type": "bool"},
        "days": {"key": "days", "type": "int"},
    }

    def __init__(self, *, enabled: bool, days: int, **kwargs: Any) -> None:
        """
        :keyword enabled: a value indicating whether the retention policy is enabled. Required.
        :paramtype enabled: bool
        :keyword days: the number of days for the retention in days. A value of 0 will retain the
         events indefinitely. Required.
        :paramtype days: int
        """
        super().__init__(**kwargs)
        self.enabled = enabled
        self.days = days


class ServiceDiagnosticSettingsResource(Resource):  # pylint: disable=too-many-instance-attributes
    """Description of a service diagnostic setting.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar storage_account_id: The resource ID of the storage account to which you would like to
     send Diagnostic Logs.
    :vartype storage_account_id: str
    :ivar service_bus_rule_id: The service bus rule ID of the service bus namespace in which you
     would like to have Event Hubs created for streaming Diagnostic Logs. The rule ID is of the
     format: '{service bus resource ID}/authorizationrules/{key name}'.
    :vartype service_bus_rule_id: str
    :ivar event_hub_authorization_rule_id: The resource Id for the event hub namespace
     authorization rule.
    :vartype event_hub_authorization_rule_id: str
    :ivar metrics: the list of metric settings.
    :vartype metrics: list[~$(python-base-namespace).v2016_09_01.models.MetricSettings]
    :ivar logs: the list of logs settings.
    :vartype logs: list[~$(python-base-namespace).v2016_09_01.models.LogSettings]
    :ivar workspace_id: The workspace ID (resource ID of a Log Analytics workspace) for a Log
     Analytics workspace to which you would like to send Diagnostic Logs. Example:
     /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2.
    :vartype workspace_id: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "storage_account_id": {"key": "properties.storageAccountId", "type": "str"},
        "service_bus_rule_id": {"key": "properties.serviceBusRuleId", "type": "str"},
        "event_hub_authorization_rule_id": {"key": "properties.eventHubAuthorizationRuleId", "type": "str"},
        "metrics": {"key": "properties.metrics", "type": "[MetricSettings]"},
        "logs": {"key": "properties.logs", "type": "[LogSettings]"},
        "workspace_id": {"key": "properties.workspaceId", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        storage_account_id: Optional[str] = None,
        service_bus_rule_id: Optional[str] = None,
        event_hub_authorization_rule_id: Optional[str] = None,
        metrics: Optional[List["_models.MetricSettings"]] = None,
        logs: Optional[List["_models.LogSettings"]] = None,
        workspace_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword storage_account_id: The resource ID of the storage account to which you would like to
         send Diagnostic Logs.
        :paramtype storage_account_id: str
        :keyword service_bus_rule_id: The service bus rule ID of the service bus namespace in which you
         would like to have Event Hubs created for streaming Diagnostic Logs. The rule ID is of the
         format: '{service bus resource ID}/authorizationrules/{key name}'.
        :paramtype service_bus_rule_id: str
        :keyword event_hub_authorization_rule_id: The resource Id for the event hub namespace
         authorization rule.
        :paramtype event_hub_authorization_rule_id: str
        :keyword metrics: the list of metric settings.
        :paramtype metrics: list[~$(python-base-namespace).v2016_09_01.models.MetricSettings]
        :keyword logs: the list of logs settings.
        :paramtype logs: list[~$(python-base-namespace).v2016_09_01.models.LogSettings]
        :keyword workspace_id: The workspace ID (resource ID of a Log Analytics workspace) for a Log
         Analytics workspace to which you would like to send Diagnostic Logs. Example:
         /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2.
        :paramtype workspace_id: str
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.storage_account_id = storage_account_id
        self.service_bus_rule_id = service_bus_rule_id
        self.event_hub_authorization_rule_id = event_hub_authorization_rule_id
        self.metrics = metrics
        self.logs = logs
        self.workspace_id = workspace_id


class ServiceDiagnosticSettingsResourcePatch(_serialization.Model):
    """Service diagnostic setting resource for patch operations.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar storage_account_id: The resource ID of the storage account to which you would like to
     send Diagnostic Logs.
    :vartype storage_account_id: str
    :ivar service_bus_rule_id: The service bus rule ID of the service bus namespace in which you
     would like to have Event Hubs created for streaming Diagnostic Logs. The rule ID is of the
     format: '{service bus resource ID}/authorizationrules/{key name}'.
    :vartype service_bus_rule_id: str
    :ivar event_hub_authorization_rule_id: The resource Id for the event hub namespace
     authorization rule.
    :vartype event_hub_authorization_rule_id: str
    :ivar metrics: the list of metric settings.
    :vartype metrics: list[~$(python-base-namespace).v2016_09_01.models.MetricSettings]
    :ivar logs: the list of logs settings.
    :vartype logs: list[~$(python-base-namespace).v2016_09_01.models.LogSettings]
    :ivar workspace_id: The workspace ID (resource ID of a Log Analytics workspace) for a Log
     Analytics workspace to which you would like to send Diagnostic Logs. Example:
     /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2.
    :vartype workspace_id: str
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "storage_account_id": {"key": "properties.storageAccountId", "type": "str"},
        "service_bus_rule_id": {"key": "properties.serviceBusRuleId", "type": "str"},
        "event_hub_authorization_rule_id": {"key": "properties.eventHubAuthorizationRuleId", "type": "str"},
        "metrics": {"key": "properties.metrics", "type": "[MetricSettings]"},
        "logs": {"key": "properties.logs", "type": "[LogSettings]"},
        "workspace_id": {"key": "properties.workspaceId", "type": "str"},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        storage_account_id: Optional[str] = None,
        service_bus_rule_id: Optional[str] = None,
        event_hub_authorization_rule_id: Optional[str] = None,
        metrics: Optional[List["_models.MetricSettings"]] = None,
        logs: Optional[List["_models.LogSettings"]] = None,
        workspace_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword storage_account_id: The resource ID of the storage account to which you would like to
         send Diagnostic Logs.
        :paramtype storage_account_id: str
        :keyword service_bus_rule_id: The service bus rule ID of the service bus namespace in which you
         would like to have Event Hubs created for streaming Diagnostic Logs. The rule ID is of the
         format: '{service bus resource ID}/authorizationrules/{key name}'.
        :paramtype service_bus_rule_id: str
        :keyword event_hub_authorization_rule_id: The resource Id for the event hub namespace
         authorization rule.
        :paramtype event_hub_authorization_rule_id: str
        :keyword metrics: the list of metric settings.
        :paramtype metrics: list[~$(python-base-namespace).v2016_09_01.models.MetricSettings]
        :keyword logs: the list of logs settings.
        :paramtype logs: list[~$(python-base-namespace).v2016_09_01.models.LogSettings]
        :keyword workspace_id: The workspace ID (resource ID of a Log Analytics workspace) for a Log
         Analytics workspace to which you would like to send Diagnostic Logs. Example:
         /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2.
        :paramtype workspace_id: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.storage_account_id = storage_account_id
        self.service_bus_rule_id = service_bus_rule_id
        self.event_hub_authorization_rule_id = event_hub_authorization_rule_id
        self.metrics = metrics
        self.logs = logs
        self.workspace_id = workspace_id
