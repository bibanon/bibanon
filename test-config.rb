require '/usr/local/src/omnigollum/lib/omnigollum'

# Providers now need to be loaded manually
require 'omniauth/strategies/github'
require 'omniauth/strategies/twitter'
require 'omniauth/strategies/facebook'

OmniAuth.config.full_host = '<url to wiki root>'

# Configure omniauth/omnigollum providers
options = {
  :providers => Proc.new do
    provider :github, "<id>", "<api token>", {:client_options => {:ssl => {:ca_path => "/etc/ssl/certs"}}}
    provider :twitter, "<id>", "<api token>", {:client_options => {:ssl => {:ca_path => "/etc/ssl/certs"}}}
  end,
  :dummy_auth => false
}

Precious::App.set(:omnigollum, options)

# Register omnigollum extension in sinatra
Precious::App.register Omnigollum::Sinatra