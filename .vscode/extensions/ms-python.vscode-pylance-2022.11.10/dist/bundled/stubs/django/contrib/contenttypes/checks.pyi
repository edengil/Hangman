from typing import Any, Optional, Sequence

from django.apps.config import AppConfig
from django.core.checks.messages import CheckMessage

def check_generic_foreign_keys(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> Sequence[CheckMessage]: ...
def check_model_name_lengths(
    app_configs: Optional[Sequence[AppConfig]] = ..., **kwargs: Any
) -> Sequence[CheckMessage]: ...
