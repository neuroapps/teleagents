for schema import (
  IntroResponse, 
  HelpResponse, 
  TelegramMessage
)

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
