Rails.application.configure do
  config.cache_classes = true
  config.eager_load = true
  config.consider_all_requests_local       = false
  config.action_controller.perform_caching = true
  config.serve_static_files = false
  config.log_level = :debug
  config.active_support.deprecation = :notify
  config.log_formatter = ::Logger::Formatter.new
  config.active_record.dump_schema_after_migration = false
end
