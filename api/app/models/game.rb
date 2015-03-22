class Game < ActiveRecord::Base
  def self.in_progress?
    where(in_progress: true).count > 0
  end
end
