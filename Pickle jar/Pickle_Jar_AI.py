import g4f, g4f.local, typing, Pickle_Jar_AI_interface, asyncio

class Pickle_Jar_LM(Pickle_Jar_AI_interface.Pickle_Jar_AI_interface):
    
    LM: typing.Final[str] = f"mistral-7b-openorca" # local LM
    PROVIDER: None = None # If you know, how to set up local provider, write it in the issue section
    
    def __init__(self: typing.Self) -> None:
        self.pickle_jar_ai_client: g4f.local.LocalClient = g4f.local.LocalClient()

    async def __response__(self: typing.Self, prompt: str) -> str:
        self.response = self.pickle_jar_ai_client.chat.completions.create(model=self.LM, messages=[{f"role": f"user", f"content": prompt}])
        
        return self.response.choices[0].message.content