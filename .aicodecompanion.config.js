// Example configuration for providing the API Endpoint:
module.exports = {
    apiProvider: {
      AzureOpenAI: {
        endPointUrl:
          "https://sfi-azureopenai-test.openai.azure.com/openai/deployments/ChatGPT4o/chat/completions?api-version=2024-04-01-preview",
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