package sample_api_provider

import "github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"

// Provider This is the entrypoint for the provider
func Provider() *schema.Provider {
	return &schema.Provider{}
}
