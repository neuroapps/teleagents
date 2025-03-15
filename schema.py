from pydantic import BaseModel
from typing import Optional, List, Union
from enum import Enum

# Empty request
class Empty(BaseModel):
    pass

# Responses
class IntroResponse(BaseModel):
    name: str
    description: str

class HelpResponse(BaseModel):
    instructions: str

# Content Types
class TextContent(BaseModel):
    text: str

class ImageContent(BaseModel):
    image_data: bytes
    caption: str
    filename: str

class VideoContent(BaseModel):
    video_data: bytes
    caption: str
    filename: str

class AudioContent(BaseModel):
    audio_data: bytes
    filename: str

class DocumentContent(BaseModel):
    file_data: bytes
    filename: str

class LocationContent(BaseModel):
    latitude: float
    longitude: float

# Enum for Telegram chat actions
class TelegramAction(str, Enum):
    UNKNOWN_ACTION = "UNKNOWN_ACTION"
    TYPING = "TYPING"
    UPLOADING_PHOTO = "UPLOADING_PHOTO"
    UPLOADING_VIDEO = "UPLOADING_VIDEO"
    UPLOADING_DOCUMENT = "UPLOADING_DOCUMENT"
    UPLOADING_AUDIO = "UPLOADING_AUDIO"
    RECORDING_VIDEO = "RECORDING_VIDEO"
    RECORDING_AUDIO = "RECORDING_AUDIO"
    UPLOADING_ANIMATION = "UPLOADING_ANIMATION"

# Button definitions for inline and reply keyboards
class InlineButton(BaseModel):
    text: str
    callback_data: str

class ReplyButton(BaseModel):
    text: str

class InlineKeyboard(BaseModel):
    buttons: List[InlineButton]

class ReplyKeyboard(BaseModel):
    buttons: List[ReplyButton]
    one_time_keyboard: Optional[bool] = False
    resize_keyboard: Optional[bool] = False

# The unified TelegramMessage
class TelegramMessage(BaseModel):
    message_id: Optional[str]
    text: Optional[TextContent]
    image: Optional[ImageContent]
    video: Optional[VideoContent]
    audio: Optional[AudioContent]
    document: Optional[DocumentContent]
    location: Optional[LocationContent]
    inline_keyboard: Optional[InlineKeyboard]
    reply_keyboard: Optional[ReplyKeyboard]
    callback_data: Optional[str]
    action: Optional[TelegramAction] = TelegramAction.UNKNOWN_ACTION

# Base class for developers to implement agents
class AgentServiceBase:
    def Intro(self) -> IntroResponse:
        """Return agent name and description."""
        raise NotImplementedError

    def Help(self) -> HelpResponse:
        """Return agent usage instructions."""
        raise NotImplementedError

    def ExecuteStream(self, request: TelegramMessage):
        """Stream response for user queries."""
        raise NotImplementedError

    def HandleCallbackStream(self, request: TelegramMessage):
        """Stream responses for callbacks."""
        raise NotImplementedError
