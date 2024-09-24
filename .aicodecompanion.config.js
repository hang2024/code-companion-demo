// Example configuration for providing the API Endpoint:
module.exports = {
    apiProvider: {
      AzureOpenAI: {
        endPointUrl:
        "https://apim-livmae.azure-api.net/gpt4/deployments/gpt4/chat/completions?api-version=2023-03-15-preview"
        //"https://apim-livmae.azure-api.net/gpt4/openai/deployments/gpt4/chat/completions?api-version=2023-03-15-preview"
        //"https://apim-livmae.azure-api.net/gtp4/openai/deployments/gtp4/chat/completions?api-version=2023-03-15-preview"
        //"https://sfi-azureopenai-test.openai.azure.com/openai/deployments/ChatGPT4o/chat/completions?api-version=2024-04-01-preview"
      },
      // Below is reference for OpenAI and PSChat Providers in case you want to change the URL for these Options. It will work only if Request and Response Contracts are same for your endpoints
      OpenAI: {
        endPointUrl: "Open AI URL",
      },
      PSChat: {
        endPointUrl: "PSChat URL",
      },
    },
  };