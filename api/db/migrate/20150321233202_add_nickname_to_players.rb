class AddNicknameToPlayers < ActiveRecord::Migration
  def change
    add_column :players, :nickname, :string, null: false
  end
end
