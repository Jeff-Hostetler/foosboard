require File.expand_path("../boot", __FILE__)

require "rails"

require "active_model/railtie"
require "active_record/railtie"
require "action_controller/railtie"

Bundler.setup(*Rails.groups)

# Enable Pry as default for `rails c`
require "pry-rails"
require "rack/cors"

module Api
  class Application < Rails::Application
    # Do not swallow errors in after_commit/after_rollback callbacks.
    config.active_record.raise_in_transactional_callbacks = true

    config.middleware.insert_before 0, "Rack::Cors" do
      allow do
        origins("*")

        resource("*", headers: :any, methods: [:get, :post, :delete, :patch, :options])
      end
    end
  end
end
